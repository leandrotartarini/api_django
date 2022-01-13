from django.test import TestCase, Client, client
from ..serializers import RecipeSerializer
from ..models import Recipe, Ingredient
from rest_framework import status

client = Client()

class GetAllRecipesTest(TestCase):

    def setUp(self):
        pass

    def test_get_all_recipes(self):
        pass

class CreateNewRecipe(TestCase):

    def setUp(self):
        pass

    def test_create_valid_recipe(self):
        pass

    def test_create_invalid_recipe(self):
        pass

class GetSingleRecipeTest(TestCase):

    def setUp(self):
        pass

    def test_get_valid_single_recipe(self):
        pass

class DeleteSingleRecipe(TestCase):

    def setUp(self):
        pass

    def test_delete_single_recipe(self):
        pass

class PutSingleRecipeTest(TestCase):

    def setUp(self):
        pass

    def test_put_single_recipe(self):
        pass