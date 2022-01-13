from rest_framework import serializers

from recipes.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe, Ingredient
        fields = "__all__"
