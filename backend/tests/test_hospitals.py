from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

class HospitalTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_hospital(self):
        url = "/hospitals/"
        data = {
            "name": "AI Hospital",
            "address": "BBSR",
            "phone": "9876543210"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)