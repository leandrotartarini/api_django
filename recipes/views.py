import traceback

from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from recipes.models import Recipe, Ingredient
from recipes.serializers import RecipeSerializer

class RecipeView(APIView):

    def get(self, request):
        try:
            recipes = Recipe.objects.all()
            serialized_recipes = RecipeSerializer(recipes, many=True).data

            return Response(serialized_recipes, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            dados = request.data
            recipe = Recipe.objects.create(
                name=dados.get("name"),
                instructions=dados.get("instructions"),
                time_to_cook=dados.get("time_to_cook")
            )
            for ingredient in dados.get("ingredients"):
                Ingredient.objects.create(
                    name=ingredient.get("name"),
                    quantity=ingredient.get("quantity"),
                    unity=ingredient.get("unity"),
                    recipe=recipe
                )

            serialized_recipe = RecipeSerializer(recipe).data
            return Response(serialized_recipe, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):

    def get(self, request, recipe_id: int):
        try:
            recipe_item = Recipe.objects.get(id=recipe_id)
            serialized_item = RecipeSerializer(recipe_item).data
            return Response(serialized_item)
        except Recipe.DoesNotExist:
            return Response({"message": "Recipe does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, recipe_id: int) -> Response:

        try:
            recipe_item = Recipe.objects.get(id=recipe_id)
            recipe_item.delete()
            return Response({"message": "Item removed successfully"})
        except Recipe.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, recipe_id):

        try:
            # o recipe_item é uma instancia (objeto) da classe Recipe
            recipe_item = Recipe.objects.get(id=recipe_id)
            recipe_item.name = request.data.get("name", recipe_item.name)
            recipe_item.instructions = request.data.get("instructions", recipe_item.instructions)
            recipe_item.time_to_cook = request.data.get("time_to_cook", recipe_item.time_to_cook)

            for ingredient in request.data.get("ingredients"):
                # ingredient_item é um dicionario
                ingredient_item = Ingredient.objects.get(id=ingredient.get("id"))
                ingredient_item.name = ingredient.get("name")
                ingredient_item.quantity = ingredient["quantity"]
                ingredient_item.unity = ingredient.get("unity")
                ingredient_item.save()

            # ingredients = Ingredient.objects.filter(recipe=recipe_item)
            # ingredients.delete()

            # for ingredient in request.data.get("ingredients"):
               # Ingredient.objects.create(
                   # name=ingredient.get("name"),
                   # quantity=ingredient.get("quantity"),
                   # unity=ingredient.get("unity"),
                   # recipe=recipe_item
               # )

            serializer = RecipeSerializer(recipe_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Recipe.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(traceback.format_exc())
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

class IngredientsDetailView(APIView):

    def patch(self, request, recipe_id):

        try:
            recipe_item = Recipe.objects.get(id=recipe_id)
            for ingredient in request.data:
                Ingredient.objects.create(
                    name=ingredient.get("name"),
                    quantity=ingredient.get("quantity"),
                    unity=ingredient.get("unity"),
                    recipe=recipe_item
                )
            serialized_recipe = RecipeSerializer(recipe_item).data
            return Response(serialized_recipe, status=status.HTTP_200_OK)

        except Recipe.DoesNotExist:
            return Response({"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
