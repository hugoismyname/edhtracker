from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import (
    AllSets ,AllView, HomeView,CardsApi, CardsView,CardDetailView,CardDetailApi,DecksRec,DecksRecApi, SearchView, SearchViewApi, UserCardCreate,
    UserCardUpdate, UserCardDelete,UserCardsListApi,UserCardsView
)

urlpatterns = [
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('api/card_detail/', CardDetailApi, name="api_card_detail"),
    path('api/user_cards/', UserCardsListApi, name="api_user_cards"),
    path('api/user_cards/<int:pk>/delete/', UserCardDelete, name="api_user_cards_delete"),
    path('api/user_cards/<int:pk>/update/', UserCardUpdate, name="api_user_cards_update"),
    path('api/cards/', CardsApi, name="user_cards_view"),
    path('api/decks_rec/', DecksRecApi, name="api_decks_rec"),    
    path('api/add_card/', UserCardCreate, name="api_add_card"),
    path('api/search/', SearchViewApi, name="api_search"),
    path('cards/<str:setCode>', CardsView, name="cards"),
    path('all', AllView.as_view() , name="all"),
    path('all_sets', AllSets , name="all_sets"),
    path('card_detail/<int:pk>', CardDetailView, name="card_detail"),
    path('decks_rec/', DecksRec, name="decks_rec"),        
    path('search/', SearchView, name="search"),
    path('user_cards/<str:username>', UserCardsView, name="user_cards"),
    path('user_cards/add/', UserCardCreate, name="user_cards_add"),
]