from rest_framework import serializers
from ..models import Pokemon, PokemonName 

class PokemonNameSerializer(serializers.ModelSerializer):
  pokemon_no = serializers.ReadOnlyField(source='pokemon_data.no', read_only=True)

  class Meta:
    model = PokemonName
    fields = ['pokemon_id', 'local_language_id', 'name', 'form_name', 'pokemon_data', 'pokemon_no']

class PokemonNameListSerializer(serializers.ListSerializer):
  child = PokemonNameSerializer()
