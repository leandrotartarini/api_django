# Generated by Django 3.2.11 on 2022-01-13 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe_id',
            new_name='recipe',
        ),
    ]
