from rest_framework import serializers
from recipes.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = "__all__"

    def get_ingredients(self, obj):
        ingredients = Ingredient.objects.filter(recipe=obj)
        return IngredientSerializer(ingredients, many=True).data
