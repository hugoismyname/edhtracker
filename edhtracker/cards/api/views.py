
from django.core import paginator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cards.models import Card, UserCards, Commander, Set
from .serializers import UserCardsSerializer, CardsSerializer, AddCardsSerializer,CommanderSerializer



def get_paginated_queryset_response(qs, request,serializer,page_size):
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = serializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data) # Response( serializer.data, status=200)

@api_view(['GET'])
def CardsApi(request, *args, **kwargs):
    set_code = request.GET.get('set')

    if set_code != None:
        allcards = Card.objects.filter(set=set_code).exclude(frame_effects__overlap=['showcase','extendedart','inverted'])
        allcards = allcards.exclude(border_color="borderless").order_by('name').values('id','img_url','name')
        white = allcards.filter(color_lookup="white").values('id','img_url','name')
        blue = allcards.filter(color_lookup="blue").values('id','img_url','name')
        black = allcards.filter(color_lookup="black").values('id','img_url','name')
        red = allcards.filter(color_lookup="red").values('id','img_url','name')
        green = allcards.filter(color_lookup="green").values('id','img_url','name')
        multicolor = allcards.filter(color_lookup="multicolor").values('id','img_url','name')
        colorless = allcards.filter(color_lookup="colorless").values('id','img_url','name')
        artifacts = allcards.filter(color_lookup="artifact").values('id','img_url','name')
        lands = allcards.filter(color_lookup="land").values('id','img_url','name')


        return Response( [white,blue,black,red,green,multicolor,colorless,artifacts,lands,allcards])
    return Response({"no set provided"}, status=404)

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

@api_view(['GET'])
def DecksRecApi(request,*args,**kwargs):
    username = request.GET.get('username')
    if username:
        uQs = UserCards.objects.filter(user_id=request.user.id).values_list('card_id',flat=True)
        user_cards = Card.objects.filter(id__in=uQs).values_list('name',flat=True)
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
        return Response(serializer.data, status=201)
    else: 
        Response({'error'}, status=500)
        print('not valid')

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
   
    user_id = request.GET.get('user_id')
    if user_id != None:
        qs = UserCards.objects.filter(user_id=user_id).select_related('card')

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
