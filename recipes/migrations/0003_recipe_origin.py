# Generated by Django 3.2.11 on 2022-02-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_recipe_id_ingredient_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='origin',
            field=models.TextField(default=''),
        ),
    ]
