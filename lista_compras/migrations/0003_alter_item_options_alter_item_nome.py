# Generated by Django 5.1.4 on 2025-01-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_compras', '0002_alter_item_options_alter_item_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['nome']},
        ),
        migrations.AlterField(
            model_name='item',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
