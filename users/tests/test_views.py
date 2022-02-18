import json
from django.test import TestCase, Client, client
from ..serializers import UserSerializer
from ..models import User
from rest_framework import status

client = Client()


class GetAllUsersTest(TestCase):

    def setUp(self):
        User.objects.create(email="testuser@test.com", password="123456")
        User.objects.create(email="testuser2@test.com", password="654321")

    def test_get_all_users(self):
        response = client.get('/user')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewUser(TestCase):

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
        response = client.post('/user/register', json.dumps(self.valid_user_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post('/user/register', json.dumps(self.invalid_user_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleUserTest(TestCase):

    def setUp(self):
        User.objects.create(email="test1user@test.com", password="123456")
        User.objects.create(email="test2user@test.com", password="654321")
        User.objects.create(email="test3user@test.com", password="135790")

        self.valid_payload = {
            "id": 2,
            "email": "test2user@test.com",
            "password": "654321"
        }

    def test_get_single_valid_user(self):
        response = client.get('/user/2')
        self.assertEqual(response.data, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSingleRecipe(TestCase):

    def setUp(self):
        User.objects.create(email="test3user@test.com", password="135790")

    def test_delete_single_user(self):
        response = client.delete('/user/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "User removed successfully"})


class PutSingleRecipeTest(TestCase):

    def setUp(self):
        User.objects.create(email="test3user@test.com", password="135790")

    def test_put_single_user(self):
        response = client.put('/user/1', {
            "email": "changedEmail@test.com",
            "password": "123456"
        }, content_type='application/json')
        valid_response = {
            'id': 1,
            'email': "changedEmail@test.com",
            "password": "123456"
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, valid_response)
