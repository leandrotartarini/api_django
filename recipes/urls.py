from django.urls import path
from recipes.views import RecipeView, RecipeDetailView, IngredientsDetailView

urlpatterns = [
    path('', RecipeView.as_view()),
    path('/<int:recipe_id>', RecipeDetailView.as_view()),
    path('/<int:recipe_id>/ingredients', IngredientsDetailView.as_view())
]