from django.urls import path
import api.views as views

urlpatterns = [
  path('pokemons/', views.PokemonListAPIView.as_view()),
  path('pokemons/<pk>/', views.PokemonAPIView.as_view()),

  path('pokemon-names/', views.PokemonNameListAPIView.as_view()),
  path('pokemon-names/<pk>/', views.PokemonNameAPIView.as_view()),

  path('health/', views.HealthAPIView.as_view()),
]