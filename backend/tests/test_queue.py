from rest_framework.test import APITestCase

class QueueTests(APITestCase):

    def test_book_slot(self):
        url = "/queue/book/"
        data = {
            "department_id": 1,
            "patient_id": 1
        }
        response = self.client.post(url, data)
        self.assertIn(response.status_code, [200, 201])