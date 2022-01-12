from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    instructions = models.TextField()
    time_to_cook = models.IntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unity = models.TextField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
