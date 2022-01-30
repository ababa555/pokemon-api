from rest_framework import serializers
from .models import Pokemon, PokemonName 

class PokemonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pokemon
    fields = ['id', 'no', 'height', 'weight', 'order', 'is_default']

class PokemonNameSerializer(serializers.ModelSerializer):
  pokemon_no = serializers.ReadOnlyField(source='pokemon_data.no', read_only=True)

  class Meta:
    model = PokemonName
    fields = ['pokemon_id', 'local_language_id', 'name', 'form_name', 'pokemon_data', 'pokemon_no']

class PokemonListSerializer(serializers.ListSerializer):
  child = PokemonSerializer()

class PokemonNameListSerializer(serializers.ListSerializer):
  child = PokemonNameSerializer()
