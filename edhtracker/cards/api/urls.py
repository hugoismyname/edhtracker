from django.urls import path
from django.conf.urls.static import static

from .views import (
    CardsApi,CardDetailApi,DecksRecApi, SearchViewApi, UserCardCreate,
    UserCardUpdate, UserCardDelete,UserCardsListApi
)

urlpatterns = [
    path('api/card_detail/', CardDetailApi, name="api_card_detail"),
    path('api/user_cards/', UserCardsListApi, name="api_user_cards"),
    path('api/user_cards/<int:pk>/delete/', UserCardDelete, name="api_user_cards_delete"),
    path('api/user_cards/<int:pk>/update/', UserCardUpdate, name="api_user_cards_update"),
    path('api/cards/', CardsApi, name="user_cards_view"),
    path('api/decks_rec/', DecksRecApi, name="api_decks_rec"),    
    path('api/add_card/', UserCardCreate, name="api_add_card"),
    path('api/search/', SearchViewApi, name="api_search")
]