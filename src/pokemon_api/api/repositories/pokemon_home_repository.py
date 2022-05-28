from abc import ABCMeta, abstractmethod
from ..models import PokemonHome

class IPokemonHomeRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, season_id, pokemon_id, type):
    pass

class PokemonHomeRepository(IPokemonHomeRepository):
  def find(self, season_id, pokemon_id, type):
    list = PokemonHome.objects.all()

    if season_id:
      list = list.filter(
        season_id = season_id
      )

    if pokemon_id:
      list = list.filter(
        pokemon_id = pokemon_id
      )

    if type:
      list = list.filter(
        type = type
      )

    return list
