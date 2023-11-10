from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestProject(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_aspirant.requests.get')
    def test_post_project(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        new_project = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": self.data_factory.random_int()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/company/project', json=new_project, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_project_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_project = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": self.data_factory.random_int()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/company/project', json=new_project, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_project(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get(
            '/abcjobs/company/project', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_project_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/company/project', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
