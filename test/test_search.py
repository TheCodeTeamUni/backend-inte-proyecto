from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestAspirant(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_aspirant.requests.get')
    def test_search_skill(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/search/Python', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_search_skill_unauthorized(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/search/Python', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 401)

    @patch('src.views.view_aspirant.requests.get')
    def test_search_skill_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/search/Python', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_search_aspirant(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/search/aspirant/1', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_search_aspirant_unauthorized(self, mock_get):
        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/search/aspirant/1', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 401)

    @patch('src.views.view_aspirant.requests.get')
    def test_search_aspirant_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/search/aspirant/1', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
