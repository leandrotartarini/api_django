from django.test import TestCase, Client, client
from ..serializers import RecipeSerializer
from ..models import Recipe, Ingredient
from rest_framework import status

client = Client()

class GetAllRecipesTest(TestCase):

    def setUp(self):
        Recipe.objects.create(name="chocolate tart", instructions="cook for one hour", time_to_cook=1)
        Recipe.objects.create(name="orange tart", instructions="cook for 2 hours", time_to_cook=5)

    def test_get_all_recipes(self):
        response = client.get('/recipe')
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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