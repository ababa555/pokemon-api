from abc import ABCMeta, abstractmethod
from ..models import PokemonName

class IPokemonNameRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version, local_language_id, name):
    pass

class PokemonNameRepository(IPokemonNameRepository):
  def find(self, id=None, version=None, local_language_id=None, name=None):
    list = PokemonName.objects.all()
    
    if version:
      list = list.filter(
        id__startswith = version + "-"
      )
 
    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    if local_language_id:
      list = list.filter(
        local_language_id = local_language_id
      )

    if name:
      list = list.filter(
        name__icontains = name
      )

    return list