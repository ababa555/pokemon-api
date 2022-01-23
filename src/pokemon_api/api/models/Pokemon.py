from django.db import models

class Pokemon(models.Model):
  class Meta:
    db_table = 'pokeomn'
    ordering = ['order']
    verbose_name = verbose_name_plural = 'ポケモン'

  id = models.CharField(primary_key=True, editable=False, max_length=5)
  no = models.IntegerField(verbose_name='No')
  height = models.IntegerField(verbose_name='高さ')
  weight = models.IntegerField(verbose_name='重さ')
  order = models.IntegerField(verbose_name='並び順')
  is_default = models.BooleanField(verbose_name='デフォルトフォルム')
  created_at = models.DateTimeField(verbose_name='登録日')

  def __str__(self):
    return self.no
