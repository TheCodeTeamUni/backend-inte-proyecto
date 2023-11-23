from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestPerformance(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_perfor.requests.get')
    def test_post_performance(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        new_performance = {
            "performance": 5
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/performance/1', json=new_performance, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_perfor.requests.get')
    def test_post_performance_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_performance = {
            "performance": 5
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/performance/1', json=new_performance, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_perfor.requests.get')
    def test_post_performance_unanthorized(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "1"
        }

        new_performance = {
            "performance": 5
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/performance/1', json=new_performance, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 401)

    @patch('src.views.view_perfor.requests.get')
    def test_get_performance(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/performance/1', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_perfor.requests.get')
    def test_get_performance_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/performance/1', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
