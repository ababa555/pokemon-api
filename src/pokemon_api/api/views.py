from django.http import Http404
from rest_framework import status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Pokemon, PokemonName
from .serializers import PokemonSerializer, PokemonNameSerializer, PokemonListSerializer, PokemonNameListSerializer

class PokemonListAPIView(views.APIView):  
  def get(self, request, format=None):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

class PokemonNameListAPIView(views.APIView):  
  def get(self, request, format=None):
    pokemonNames = PokemonName.objects.all()
    serializer = PokemonNameSerializer(pokemonNames, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

class PokemonAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonSerializer(pokemon)
    return Response(serializer.data, status.HTTP_200_OK)

class PokemonNameAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      pokemonName = PokemonName.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonNameSerializer(pokemonName)
    return Response(serializer.data, status.HTTP_200_OK)