from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('pokemons/', views.PokemonListAPIView.as_view()),
  path('pokemons/<pk>/', views.PokemonAPIView.as_view()),
  path('pokemon-names/', views.PokemonNameListAPIView.as_view()),
  path('pokemon-names/<pk>/', views.PokemonNameAPIView.as_view()),
]