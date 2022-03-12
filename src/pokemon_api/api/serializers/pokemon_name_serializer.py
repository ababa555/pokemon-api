import re
from rest_framework import serializers
from ..models import Pokemon, PokemonName 

class PokemonNameSerializer(serializers.ModelSerializer):
  pokemon_no = serializers.ReadOnlyField(source='pokemon.no', read_only=True)

  class Meta:
    model = PokemonName
    fields = ['id', 'local_language_id', 'name', 'form_name', 'pokemon_id', 'pokemon_no']

  def create(self, validated_data):
    id = validated_data['id']
    repatter = re.compile('^.*-')
    result = repatter.match(id)
    # ex:n1-1⇒n1
    pokemon = Pokemon.objects.get(pk=id[result.start():result.end()-1])
    
    pokemonName = PokemonName.objects.create(
      id=id, 
      local_language_id=validated_data['local_language_id'], 
      name=validated_data['name'], 
      form_name=validated_data['form_name'] if validated_data['form_name'] != '""' else '',
      pokemon_id=pokemon.id)
    return pokemonName

class PokemonNameListSerializer(serializers.ListSerializer):
  child = PokemonNameSerializer()
