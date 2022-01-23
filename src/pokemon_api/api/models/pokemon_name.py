from django.db import models

from . import Pokemon

class PokemonName(models.Model):
  class Meta:
    db_table = 'pokemon_name'
    ordering = ['pokemon_id', 'local_language_id']
    verbose_name = verbose_name_plural = 'ポケモン名'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "local_language_id"],
        name="unique_pokemon_name"
      ),
    ]

  pokemon_id = models.CharField(verbose_name='ポケモンID', max_length=5)
  local_language_id = models.IntegerField(verbose_name='言語')
  name = models.CharField(verbose_name='ポケモン名', max_length=10)
  form_name = models.CharField(verbose_name='フォルム名', max_length=20)

  pokemon_data = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    name = self.name
    form_name = '' if self.form_name == '' else '（{}）'.format(self.form_name)
    return name + form_name
