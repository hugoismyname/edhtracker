from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView, FormView
from .models import Card, UserCards, Commander, Set
from .api.serializers import UserCardsSerializer, CardsSerializer, AddCardsSerializer,CommanderSerializer

from collections import Counter 

def get_paginated_queryset_response(qs, request,serializer,page_size):
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = serializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data) # Response( serializer.data, status=200)

def AllSets(request, *args, **kwargs):
    all_sets = Set.objects.exclude(digital=True).exclude(set_type='token').values('code','id','img_url','name','released_at','set_type').order_by('-released_at')
    return render(request, "cards/all_sets.html",{'sets':all_sets})

@api_view(['GET'])
def CardsApi(request, *args, **kwargs):
    set_code = request.GET.get('set')

    if set_code != None:
        qs = Card.objects.filter(set__iexact=set_code).exclude(frame_effects__overlap=['showcase','extendedart','inverted']).exclude(border_color="borderless").order_by('name')
        allcards = CardsSerializer(qs, many=True)
        wqs = qs.filter(color_lookup="white")
        uqs = qs.filter(color_lookup="blue")
        bqs = qs.filter(color_lookup="black")
        rqs = qs.filter(color_lookup="red")
        gqs = qs.filter(color_lookup="green")
        mqs = qs.filter(color_lookup="multicolor")
        cqs = qs.filter(color_lookup="").exclude(type_line__icontains="land").exclude(type_line__icontains="artifact")
        aqs = qs.filter(color_lookup="").filter(type_line__icontains="artifact")
        lqs = qs.filter(type_line__icontains="land")
        white = CardsSerializer(wqs,many=True)
        blue = CardsSerializer(uqs,many=True)
        black = CardsSerializer(bqs,many=True)
        red = CardsSerializer(rqs,many=True)
        green = CardsSerializer(gqs,many=True)
        multicolor = CardsSerializer(mqs,many=True)
        colorless = CardsSerializer(cqs,many=True)
        artifact = CardsSerializer(aqs,many=True)
        lands = CardsSerializer(lqs,many=True)
        return Response( [white.data,blue.data,black.data,red.data,green.data,multicolor.data,colorless.data,artifact.data,lands.data,allcards.data])

def CardsView(request,setCode, *args, **kwargs):
    qs = Set.objects.filter(code=setCode).first()
    setName = qs.name
    return render(request, "cards/cards.html",{'setCode':setCode,'setName':setName})

@api_view(['GET'])
def CardDetailApi(request,*args,**kwargs):
    pk = request.GET.get('pk')
    username = request.GET.get('username') or None

    deck = Commander.objects.filter(commander_id=pk).first()
    deck_list = (Card.objects
                    .filter(name__in=deck.card_list)
                    .exclude(frame_effects__overlap=['showcase','extendedart','inverted'])
                    .exclude(border_color="borderless").order_by('name')
                    .distinct('name')
                    .values('id','img_url','name','type_line'))

    def sort_by_type(card_query):
        artifacts = []
        creatures = []
        enchantments = []
        instants = []
        lands = []
        planeswalkers = []
        sorceries = []
        for item in card_query:
            if 'Creature' in item['type_line']:
                creatures.append(item)
            elif 'Artifact' in item['type_line']:
                artifacts.append(item)
            elif 'Enchantment' in item['type_line']:
                enchantments.append(item)
            elif 'Instant' in item['type_line']:
                instants.append(item)
            elif 'Land' in item['type_line']:
                lands.append(item)
            elif 'Planeswalker' in item['type_line']:
                planeswalkers.append(item)
            elif 'Sorcery' in item['type_line']:
                sorceries.append(item)
            else:
                continue

        deck_data = [
                {'creatures': CardsSerializer(creatures,many=True).data},
                {'instants': CardsSerializer(instants,many=True).data},
                {'sorceries': CardsSerializer(sorceries,many=True).data}, 
                {'artifacts': CardsSerializer(artifacts,many=True).data},
                {'enchantments': CardsSerializer(enchantments,many=True).data},
                {'planeswalkers': CardsSerializer(planeswalkers,many=True).data},
                {'lands': CardsSerializer(lands,many=True).data}
        ]
        return deck_data

    if username:
        user_list = UserCards.objects.filter(user_id=request.user.id).values_list('name',flat=True)
        cards_owned = deck_list.filter(name__in=user_list[:1000]).values('id','img_url','name','type_line')
        cards_needed = deck_list.exclude(name__in=user_list[:1000]).values('id','img_url','name','type_line')
        return Response([sort_by_type(cards_needed),sort_by_type(cards_owned)], status=200)
    else:
        cards_data = sort_by_type(deck_list)
        return Response(cards_data, status=200)

def CardDetailView(request,pk, *args,**kwargs):
    card = Card.objects.filter(id=pk).values('id','img_url','is_commander','type_line','oracle_text','flavor_text','name','set').first()
    user_card = UserCards.objects.filter(card_id=pk).first()
    set_info = Set.objects.filter(code=card['set']).values('img_url').first()

    context = {
        'card':card,
        'set_info':set_info,
        'user_card':user_card,
        'pk':pk
    }
    return render(request, "cards/card_detail.html",context)


class AllView(ListView):
    queryset = Card.objects.filter(is_commander=True).exclude(set_type="funny").exclude(set_type="memorabilia").order_by('name').distinct('name')
    # model = Card
    paginate_by = 1000
    template_name = "cards/all_cards.html"
    
    ordering = ['name']

def DecksRec(request, *args, **kwargs):
    return render(request, "cards/decks_rec.html")

@api_view(['GET'])
def DecksRecApi(request,*args,**kwargs):
    username = request.GET.get('username')
    if username:
        uQs = UserCards.objects.filter(user_id=request.user.id).values('name')[:150]
        user_cards = [i['name'] for i in uQs]

        commanders = Commander.objects.all().values_list('card_list','commander_id','img_url','name')

        keys = ['total_cards','id','img_url','name','cards_owned']
        commander_data =[]

        for commander in commanders:
            temp_data = []
            
            cards_owned = len(set(user_cards).intersection(commander[0]))

            temp_data.append(len(commander[0])) 
            temp_data.append(commander[1])
            temp_data.append(commander[2])
            temp_data.append(commander[3])
            temp_data.append(cards_owned)

            commander_data.append(dict(zip(keys, temp_data)))
            new_commander_data = sorted(commander_data, reverse=True ,key=lambda k: k['cards_owned'])
        
        return Response(new_commander_data, status=200)
    else:
        return Response({"No content"}, status=204)

def HomeView(request, *args, **kwargs):
    return render(request, "cards/home.html")

def SearchView(request, *args, **kwargs):
    searchParam = request.GET.get('searchParam')
    return render(request, "cards/search.html",{'searchParam':searchParam})

@api_view(['GET'])
def SearchViewApi(request, *args, **kwargs):
    searchParam = request.GET.get('searchParam')
    if searchParam != None:
        qs = Card.objects.filter(name__icontains=searchParam).order_by('name')
        return get_paginated_queryset_response(qs,request,CardsSerializer,100)
    
@api_view(['POST','UPDATE'])
@permission_classes([IsAuthenticated])
def UserCardCreate(request,*args,**kwargs):
    serializer = AddCardsSerializer(data=request.data or None)
    if serializer.is_valid():
        serializer.save(user=request.user)
        print(request.user)
        return Response(serializer.data, status=201)
    else: Response({serializer}, status=500)

@api_view(['POST','DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def UserCardDelete(request,pk=None,*args,**kwargs):
    qs = UserCards.objects.filter(id=pk)
    if not qs.exists():
        return Response({"message": "You cannot delete this card"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Card Removed"}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserCardsListApi(request, *args, **kwargs):
    qs = UserCards.objects.all()
    username = request.GET.get('username')
    if username != None:
       qs = qs.filter(user__username__iexact=username)

    return get_paginated_queryset_response(qs,request,UserCardsSerializer,200)

@api_view(['POST','UPDATE'])
@permission_classes([IsAuthenticated])
def UserCardUpdate(request,pk=None,*args,**kwargs):
    qs = UserCards.objects.filter(id=pk)
    if not qs.exists():
        return Response({"message": "You cannot update this card"}, status=401)
    obj = qs.first()
    obj.card_count = request.data['card_count']
    obj.save()
    return Response({"message": "Card Updated"}, status=204)

def UserCardsView(request, *args, **kwargs):
    return render(request, "cards/usercards.html")