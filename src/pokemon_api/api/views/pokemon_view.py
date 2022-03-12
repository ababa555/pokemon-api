from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response
from ..models import Pokemon
from ..serializers import PokemonSerializer, PokemonListSerializer

class PokemonListAPIView(views.APIView):  
  def get(self, request, format=None):
    pokemons = Pokemon.objects.all()
    serializer = PokemonListSerializer(pokemons)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonListSerializer(data=request.data)
    pokemons = Pokemon.objects.all()
    pokemons.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonSerializer(pokemon)
    return Response(serializer.data, status.HTTP_200_OK)

