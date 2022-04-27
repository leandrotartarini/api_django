import json
from django.test import Client
from recipes.tests.test_views import BaseTest
from ..serializers import UserSerializer
from ..models import User
from rest_framework import status
client = Client()


class GetAllUsersTest(BaseTest):

    def setUp(self):
        self.valid_user_payload = {
            'email': 'testuser@test.com',
            'password': '123456'
        }

    def test_user_must_send_jwt_token(self):
        response = client.get('/user')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_users(self):
        response = client.get('/user', **self.bearer_token)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class CreateNewUser(BaseTest):

    def setUp(self):
        self.valid_user_payload = {
            'email': 'testValid@valid.com',
            'password': '1v2a3l4i5d6'
        }

        self.invalid_user_payload = {
            'email': 'testInvalid@invalid.com',
            'password': ''
        }

    def test_create_valid_user(self):
        response = client.post('/user/register', json.dumps(self.valid_user_payload),
                               content_type="application/json", **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post('/user/register', json.dumps(self.invalid_user_payload),
                               content_type="application/json", **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleUserTest(BaseTest):

    def setUp(self):
        User.objects.create(email="test1user@test.com", password="123456")
        User.objects.create(email="test2user@test.com", password="654321")
        User.objects.create(email="test3user@test.com", password="135790")

        self.valid_payload = {
            "id": 2,
            "email": "test2user@test.com"
        }

    def test_get_single_valid_user(self):
        response = client.get('/user/2', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.valid_payload)


class DeleteSingleRecipe(BaseTest):

    def test_delete_single_user(self):
        response = client.delete('/user/1', **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "User removed successfully"})


class PutSingleRecipeTest(BaseTest):

    def setUp(self):
        User.objects.create(email="test3user@test.com", password="135790")
        User.objects.create(email="test4user@test.com", password="246800")

    def test_put_email(self):
        response = client.put('/user/1', {
            "email": "changedEmail@test.com",
        }, content_type='application/json', **self.bearer_token)
        valid_response = {
            'id': 1,
            'email': "changedEmail@test.com"
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, valid_response)

    def test_put_password(self):
        response = client.put('/user/2', {
            "password": "newpassword123",
        }, content_type='application/json', **self.bearer_token)
        valid_response = {
            'id': 2,
            'email': 'test4user@test.com'
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, valid_response)

