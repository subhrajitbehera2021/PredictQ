from django.urls import reverse
from rest_framework.test import APITestCase

class AuthTests(APITestCase):

    def test_register(self):
        url = reverse('register')
        data = {
            "username": "testuser1",
            "email": "test1@gmail.com",
            "password": "Test1@123",
            "role": "super_admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.test_register()
        url = reverse('login')
        data = {
            "username": "testuser1",
            "password": "Test1@123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)