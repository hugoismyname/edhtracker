from django.urls import path
from django.conf.urls.static import static

from .views import (
    AllSets ,AllView, CardsView,CardDetailView,DecksRec, SearchView,
    UserCardsView
)

urlpatterns = [
    path('cards/<str:setCode>', CardsView, name="cards"),
    path('all', AllView.as_view() , name="all"),
    path('all_sets', AllSets , name="all_sets"),
    path('card_detail/<int:pk>', CardDetailView, name="card_detail"),
    path('decks_rec/', DecksRec, name="decks_rec"),        
    path('search/', SearchView, name="search"),
    path('user_cards/<str:username>', UserCardsView, name="user_cards"),
]