# Generated by Django 2.2.3 on 2020-03-25 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20200325_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokemon_entities', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]
