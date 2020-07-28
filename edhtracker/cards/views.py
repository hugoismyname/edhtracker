from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView
from .models import Card, UserCards, Commander, Set


def AllSets(request, *args, **kwargs):
    all_sets = Set.objects.exclude(digital=True).exclude(set_type='token').values('code','id','img_url','name','released_at','set_type').order_by('-released_at')
    return render(request, "cards/all_sets.html",{'sets':all_sets})

def CardsView(request,setCode, *args, **kwargs):
    qs = Set.objects.filter(code=setCode).first()
    setName = qs.name
    return render(request, "cards/cards.html",{'setCode':setCode,'setName':setName})

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

def HomeView(request, *args, **kwargs):
    return render(request, "cards/home.html")

def SearchView(request, *args, **kwargs):
    searchParam = request.GET.get('searchParam')
    return render(request, "cards/search.html",{'searchParam':searchParam})

def UserCardsView(request, *args, **kwargs):
    user_id = request.user.id
    context = {
        'user_id': user_id
    }
    return render(request, "cards/usercards.html", context=context)