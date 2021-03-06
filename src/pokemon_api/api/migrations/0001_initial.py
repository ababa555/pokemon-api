# Generated by Django 4.0.1 on 2022-05-28 13:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, verbose_name='技名')),
                ('type', models.CharField(max_length=1, verbose_name='タイプ')),
                ('power1', models.CharField(max_length=3, verbose_name='威力1')),
                ('power2', models.CharField(max_length=3, verbose_name='威力2')),
                ('pp', models.CharField(max_length=2, verbose_name='PP')),
                ('accuracy', models.CharField(max_length=3, verbose_name='命中')),
                ('priority', models.CharField(max_length=3, verbose_name='優先度')),
                ('damage_type', models.CharField(max_length=3, verbose_name='分類')),
                ('is_direct', models.BooleanField(verbose_name='直接')),
                ('can_protect', models.BooleanField(verbose_name='守る')),
            ],
            options={
                'verbose_name': '技',
                'verbose_name_plural': '技',
                'db_table': 'move',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('no', models.IntegerField(verbose_name='No')),
                ('height', models.CharField(max_length=10, verbose_name='高さ')),
                ('weight', models.CharField(max_length=10, verbose_name='重さ')),
                ('order', models.IntegerField(verbose_name='並び順')),
                ('is_default', models.BooleanField(verbose_name='デフォルトフォルム')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
            ],
            options={
                'verbose_name': 'ポケモン',
                'verbose_name_plural': 'ポケモン',
                'db_table': 'pokemon',
                'ordering': ['no', 'order'],
            },
        ),
        migrations.CreateModel(
            name='PokemonHome',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('season_id', models.CharField(max_length=5)),
                ('pokemon_id', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('WAZA', 0), ('TOKUSEI', 1), ('SEIKAKU', 2), ('MOTIMONO', 3)], max_length=8, verbose_name='データ種別')),
                ('pokemon_name', models.CharField(max_length=30, verbose_name='ポケモン名')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('percent', models.FloatField(verbose_name='使用率')),
            ],
            options={
                'verbose_name': 'PokemonHOMEデータ',
                'verbose_name_plural': 'PokemonHOMEデータ',
                'db_table': 'pokemon_home',
            },
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('type_id', models.CharField(max_length=2, verbose_name='タイプ')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモンタイプ',
                'verbose_name_plural': 'ポケモンタイプ',
                'db_table': 'pokemon_type',
                'ordering': ['id', 'type_id'],
            },
        ),
        migrations.CreateModel(
            name='PokemonStats',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('hp', models.IntegerField(verbose_name='HP')),
                ('attack', models.IntegerField(verbose_name='こうげき')),
                ('defense', models.IntegerField(verbose_name='ぼうぎょ')),
                ('sp_attack', models.IntegerField(verbose_name='とくこう')),
                ('sp_defense', models.IntegerField(verbose_name='とくぼう')),
                ('speed', models.IntegerField(verbose_name='すばやさ')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモン種族値',
                'verbose_name_plural': 'ポケモン種族値',
                'db_table': 'pokemon_stats',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PokemonName',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('local_language_id', models.IntegerField(verbose_name='言語')),
                ('name', models.CharField(max_length=10, verbose_name='ポケモン名')),
                ('form_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='フォルム名')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモン名',
                'verbose_name_plural': 'ポケモン名',
                'db_table': 'pokemon_name',
                'ordering': ['pokemon_id', 'local_language_id'],
            },
        ),
        migrations.CreateModel(
            name='PokemonMove',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('move_name', models.CharField(max_length=10, verbose_name='技名')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモン技',
                'verbose_name_plural': 'ポケモン技',
                'db_table': 'pokemon_move',
                'ordering': ['id', 'move_name'],
            },
        ),
        migrations.CreateModel(
            name='PokemonEvolutionChain',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('evolution_chain_id', models.CharField(max_length=10, verbose_name='特性名')),
                ('order', models.IntegerField(verbose_name='並び順')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモン進化',
                'verbose_name_plural': 'ポケモン進化',
                'db_table': 'pokemon_evolution_chain',
                'ordering': ['id', 'evolution_chain_id'],
            },
        ),
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ability_name', models.CharField(max_length=10, verbose_name='特性名')),
                ('is_hidden', models.BooleanField(verbose_name='隠れ特性')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon', verbose_name='ポケモン')),
            ],
            options={
                'verbose_name': 'ポケモン特性',
                'verbose_name_plural': 'ポケモン特性',
                'db_table': 'pokemon_ability',
                'ordering': ['id', 'ability_name'],
            },
        ),
        migrations.AddConstraint(
            model_name='pokemontype',
            constraint=models.UniqueConstraint(fields=('pokemon_id', 'type_id'), name='unique_pokemon_type'),
        ),
        migrations.AddConstraint(
            model_name='pokemonname',
            constraint=models.UniqueConstraint(fields=('pokemon_id', 'local_language_id'), name='unique_pokemon_name'),
        ),
        migrations.AddConstraint(
            model_name='pokemonmove',
            constraint=models.UniqueConstraint(fields=('pokemon_id', 'move_name'), name='unique_pokemon_move'),
        ),
        migrations.AddConstraint(
            model_name='pokemonevolutionchain',
            constraint=models.UniqueConstraint(fields=('pokemon_id', 'evolution_chain_id'), name='unique_pokemon_evolution_chain'),
        ),
        migrations.AddConstraint(
            model_name='pokemonability',
            constraint=models.UniqueConstraint(fields=('pokemon_id', 'ability_name'), name='unique_pokemon_ability'),
        ),
    ]
