from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    instructions = models.TextField()
    time_to_cook = models.IntegerField()
    origin = models.TextField(default="")


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unity = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
