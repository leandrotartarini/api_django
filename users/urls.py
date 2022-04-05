from django.urls import path
from users.views import UserRegistrationView, UserView, UserViewDetail, UserRecipesView

urlpatterns = [
    path('/register', UserRegistrationView.as_view()),
    path('', UserView.as_view()),
    path('/<int:user_id>', UserViewDetail.as_view()),
    path('/recipes', UserRecipesView.as_view())
]
