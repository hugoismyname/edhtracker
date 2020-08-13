from django.db.models import Prefetch
from django.core import paginator
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cards.models import Card, UserCards, Commander, Set
from .serializers import (
    UserCardsSerializer,
    CardsSerializer,
    AddCardsSerializer,
    CommanderSerializer,
)


def get_paginated_queryset_response(qs, request, serializer, page_size):
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = serializer(paginated_qs, many=True)
    return paginator.get_paginated_response(
        serializer.data
    )  # Response( serializer.data, status=200)


@api_view(["GET"])
def CardsApi(request, *args, **kwargs):
    set_code = request.GET.get("set")

    if set_code != None:
        allcards = Card.objects.filter(set=set_code).filter(is_variation=False)
        allcards = allcards.values("id", "img_url", "name")
        white = (
            allcards.filter(color_lookup="white")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        blue = (
            allcards.filter(color_lookup="blue")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        black = (
            allcards.filter(color_lookup="black")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        red = (
            allcards.filter(color_lookup="red")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        green = (
            allcards.filter(color_lookup="green")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        multicolor = (
            allcards.filter(color_lookup="multicolor")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        colorless = (
            allcards.filter(color_lookup="colorless")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        artifacts = (
            allcards.filter(color_lookup="artifact")
            .values("id", "img_url", "name")
            .order_by("name")
        )
        lands = (
            allcards.filter(color_lookup="land")
            .values("id", "img_url", "name")
            .order_by("name")
        )

        return Response(
            [
                white,
                blue,
                black,
                red,
                green,
                multicolor,
                colorless,
                artifacts,
                lands,
                allcards,
            ]
        )
    return Response({"no set provided"}, status=404)


@api_view(["GET"])
def CardDetailApi(request, *args, **kwargs):
    pk = request.GET.get("pk")
    username = request.GET.get("username") or None
    commander_list = Commander.objects.get(commander_id=pk)
    commander_list = commander_list.card_list

    if username and request.user.is_authenticated:
        cards_owned_names = UserCards.objects.filter(
            card__name__in=commander_list
        ).order_by("card__name")
        cards_owned_names = cards_owned_names.distinct("card__name").values_list(
            "card__name", flat=True
        )

        cards_owned = Card.objects.filter(name__in=commander_list).filter(
            name__in=cards_owned_names
        )
        cards_owned = (
            cards_owned.order_by("name")
            .distinct("name")
            .values("name", "id", "img_url", "type")
        )

        cards_needed = Card.objects.filter(name__in=commander_list).exclude(
            # remove this only for testing
            name__in=cards_owned_names[:50]
        )
        cards_needed = (
            cards_needed.order_by("name")
            .distinct("name")
            .values("name", "id", "img_url", "type")
        )

        return Response({cards_needed, cards_owned}, status=200)
    else:
        all_cards = (
            Card.objects.filter(name__in=commander_list)
            .order_by("name", "type")
            .distinct("name")
            .values("name", "id", "img_url", "type")
        )
        return Response(all_cards, status=200)


@api_view(["GET"])
def DecksRecApi(request, *args, **kwargs):
    username = request.GET.get("username")
    if username:
        try:
            user_cards = UserCards.objects.filter(user_id=request.user.id).values_list(
                "card__name", flat=True
            )

            commanders = Commander.objects.all().order_by("name").distinct("name")
            commanders = commanders.values_list(
                "card_list", "commander_id", "img_url", "name"
            )

            keys = ["total_cards", "id", "img_url", "name", "cards_owned"]
            commander_data = []
            # limiting to 100 commanders remove during production and eventually switch to showuing only 100
            # most popular commanders
            for commander in commanders[:100]:
                temp_data = []
                # limiting to 10000 cards remove during production
                cards_owned = len(set(user_cards[:10000]).intersection(commander[0]))

                temp_data.append(len(commander[0]))
                temp_data.append(commander[1])
                temp_data.append(commander[2])
                temp_data.append(commander[3])
                temp_data.append(cards_owned)

                commander_data.append(dict(zip(keys, temp_data)))
                new_commander_data = sorted(
                    commander_data, reverse=True, key=lambda k: k["cards_owned"]
                )

            return Response(new_commander_data[:100], status=200)
        except:
            return Response({"No content"}, status=204)
    else:
        return Response({"No content"}, status=204)


@api_view(["GET"])
def SearchViewApi(request, *args, **kwargs):
    searchParam = request.GET.get("searchParam")
    if searchParam != None:
        qs = (
            Card.objects.filter(name__icontains=searchParam)
            .order_by("name")
            .values("name", "id", "img_url")
        )
        if qs:
            return get_paginated_queryset_response(qs, request, CardsSerializer, 100)
        else:
            return Response({"No content"}, status=204)
    else:
        return Response({"No content"}, status=204)


@api_view(["POST", "UPDATE"])
@permission_classes([IsAuthenticated])
def UserCardCreate(request, *args, **kwargs):
    serializer = AddCardsSerializer(data=request.data or None)
    print(request.user)
    if serializer.is_valid():
        card = (
            UserCards.objects.filter(user_id=request.user)
            .filter(card_id=request.data["card"])
            .exists()
        )
        if card:
            new_card = UserCards.objects.get(
                user_id=request.user, card_id=request.data["card"]
            )
            new_card.card_count = new_card.card_count + request.data["card_count"]
            new_card.save()
        else:
            serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    else:
        return Response({"error"}, status=500)


@api_view(["POST", "DELETE", "GET"])
@permission_classes([IsAuthenticated])
def UserCardDelete(request, pk=None, *args, **kwargs):
    qs = UserCards.objects.filter(id=pk)
    if not qs.exists():
        return Response({"message": "You cannot delete this card"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Card Removed"}, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def UserCardsListApi(request, *args, **kwargs):

    user_id = request.GET.get("user_id")
    # test query with more cards in usercards
    if user_id != None:
        qs = UserCards.objects.filter(user_id=user_id).select_related("card")
        qs = qs.values(
            "card_id",
            "card_count",
            "date_added",
            "card__name",
            "card__img_url",
            "card__set",
            "card__type_line",
            "id",
        )
    return get_paginated_queryset_response(qs, request, UserCardsSerializer, 200)


@api_view(["POST", "UPDATE"])
@permission_classes([IsAuthenticated])
def UserCardUpdate(request, pk=None, *args, **kwargs):
    qs = UserCards.objects.filter(id=pk)
    if not qs.exists():
        return Response({"message": "You cannot update this card"}, status=401)
    obj = qs.first()
    obj.card_count = request.data["card_count"]
    obj.save()
    return Response({"message": "Card Updated"}, status=204)
