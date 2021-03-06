from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view

from django.views.generic import ListView
from .models import Card, UserCards, Commander, Set

from itertools import groupby


def AllSets(request, *args, **kwargs):
    all_sets = (
        Set.objects.exclude(digital=True)
        .exclude(set_type="token")
        .exclude(set_type="promo")
        .values("code", "id", "img_url", "name", "released_at", "set_type")
        .order_by("set_type", "-released_at")
    )

    return render(request, "cards/all_sets.html", {"all_sets": all_sets})


def CardsView(request, setCode, *args, **kwargs):
    qs = get_object_or_404(Set, code=setCode)
    setName = qs.name
    return render(request, "cards/cards.html", {"setCode": setCode, "setName": setName})


def CardDetailView(request, pk, *args, **kwargs):
    card = (
        Card.objects.filter(id=pk)
        .values(
            "id",
            "img_url",
            "is_commander",
            "type_line",
            "oracle_text",
            "flavor_text",
            "name",
            "set",
        )
        .first()
    )
    if card:
        all_versions = Card.objects.filter(name=card["name"]).values(
            "artist", "id", "img_url", "name", "set",
        )
        set_info = Set.objects.filter(code=card["set"]).values("img_url").first()

        if request.user.is_authenticated:
            user_card = UserCards.objects.filter(card_id=pk).count()
        else:
            user_card = 0
        context = {
            "all_versions": all_versions,
            "card": card,
            "set_info": set_info,
            "user_card": user_card,
            "pk": pk,
        }
        return render(request, "cards/card_detail.html", context)
    else:
        return redirect("/")


def DecksRec(request, *args, **kwargs):
    return render(request, "cards/decks_rec.html")


def HomeView(request, *args, **kwargs):
    return render(request, "cards/home.html")


def SearchView(request, *args, **kwargs):
    searchParam = request.GET.get("searchParam")
    print(searchParam)
    return render(request, "cards/search.html", {"searchParam": searchParam})


def UserCardsView(request, *args, **kwargs):
    user_id = request.user.id
    context = {"user_id": user_id}
    return render(request, "cards/usercards.html", context=context)
