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
        self.valid_payload = {
            'name': 'double chocolate tart',
            'instructions': 'cook for three hours',
            'time_to_cook': 1,
            'ingredients': [
                {
                    "name": "banana",
                    "quantity": "2",
                    "unity": "300g"
                },
                {
                    "name": "condensed milk",
                    "quantity": "1",
                    "unity": "400g"
                }
            ]}
        self.invalid_payload = {
            'name': 'double chocolate tart',
            'instructions': 'cook for three hours',
            'time_to_cook': 1,
            'ingredients': []
        }

    def test_create_valid_recipe(self):
        pass
        # response = client.post('/recipe', self.valid_payload)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_recipe(self):
        pass
        # response = client.post('/recipe', self.invalid_payload)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleRecipeTest(TestCase):

    def setUp(self):
        self.choc_tart = Recipe.objects.create(name="chocolate tart", instructions="cook for one hour", time_to_cook=1)
        self.double_choc = Recipe.objects.create(name="double chocolate tart", instructions="cook for three hours",
                                                 time_to_cook=3)
        self.triple_choc = Recipe.objects.create(name="double chocolate tart", instructions="cook for four hours",
                                                 time_to_cook=4)

        self.valid_payload = {
            'id': 2,
            'ingredients': [],
            'name': 'double chocolate tart',
            'instructions': 'cook for three hours',
            'time_to_cook': 3
        }

    def test_get_valid_single_recipe(self):
        response = client.get('/recipe/2')
        self.assertEqual(response.data, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSingleRecipe(TestCase):

    def setUp(self):
        self.choc_tart = Recipe.objects.create(name="chocolate tart", instructions="cook for one hour", time_to_cook=1)

    def test_delete_single_recipe(self):
        response = client.delete('/recipe/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Item removed successfully"})


class PutSingleRecipeTest(TestCase):

    def setUp(self):
        self.choc_tart = Recipe.objects.create(name="chocolate tart", instructions="cook for one hour", time_to_cook=1)

    def test_put_single_recipe(self):
        response = client.put('/recipe/1', {
            'name': "banana tart",
            'instructions': "cook for two hours",
            'time_to_cook': 2,
            'ingredients': []
        }, content_type='application/json')
        valid_response = {
            'id': 1,
            'ingredients': [],
            'name': "banana tart",
            'instructions': "cook for two hours",
            'time_to_cook': 2,
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, valid_response)
