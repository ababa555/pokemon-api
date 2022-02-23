from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response
from ..models import Pokemon, PokemonName
from ..serializers import PokemonNameSerializer, PokemonNameListSerializer

# http://127.0.0.1:8000/api/pokemon-names/?name=あ
class PokemonNameListAPIView(views.APIView):  
  def get(self, request, format=None):
    print(request.query_params)
    
    local_language_id = request.query_params.get('local_language_id')
    if local_language_id:
      pokemonNames = PokemonName.objects.filter(
        local_language_id=local_language_id
      )

    name = request.query_params.get('name')
    if name:
      pokemonNames = PokemonName.objects.filter(
        name__icontains=name
      )

    serializer = PokemonNameListSerializer(pokemonNames)
    return Response(serializer.data, status.HTTP_200_OK)

class PokemonNameAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      pokemonName = PokemonName.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonNameSerializer(pokemonName)
    return Response(serializer.data, status.HTTP_200_OK)