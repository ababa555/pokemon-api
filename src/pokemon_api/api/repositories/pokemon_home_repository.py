from abc import ABCMeta, abstractmethod
from ..models import PokemonHome

class IPokemonHomeRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, season_id, pokemon_id):
    pass

class PokemonHomeRepository(IPokemonHomeRepository):
  def find(self, season_id, pokemon_id):
    list = PokemonHome.objects.filter(season_id=season_id, pokemon_id=pokemon_id).order_by('type', '-percent')

    return list