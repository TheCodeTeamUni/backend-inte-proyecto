import json
from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestUsuario(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.views.requests.post')
    def test_signup_successful(self, mock_post):

        signup_data = {
            "id": 1,
            "createdAt": "2023-10-14T15:47:05"
        }

        new_user = {
            "username": self.data_factory.name(),
            "email": self.data_factory.email(),
            "password": self.data_factory.password(),
            "type": self.data_factory.random_element(elements=('1', '2'))
        }

        mock_post.return_value.json.return_value = signup_data
        mock_post.return_value.status_code = 201

        response = self.client.post('/abcjobs/signup', json=new_user)

        self.assertEqual(response.json, signup_data)
        self.assertEqual(response.status_code, 201)

    def test_signup_missing_fields(self):

        new_user = {
            "username": self.data_factory.name(),
            "email": self.data_factory.email(),
            "password": self.data_factory.password(),
        }

        response = self.client.post('/abcjobs/signup', json=new_user)

        self.assertEqual(response.json['mensaje'],
                         'Por favor ingresar todos los campos')
        self.assertEqual(response.status_code, 400)

    def test_fail_page(self):

        endpoint_usuario = "/abcjobs/fail"
        headers = {'Content-Type': 'application/json'}

        sol_logUser = self.client.get(endpoint_usuario,
                                      headers=headers)

        self.assertEqual(sol_logUser.status_code, 404)

    def test_ping_users(self):

        endpoint_ping = "/"
        headers = {'Content-Type': 'application/json'}

        sol_ping = self.client.get(endpoint_ping,
                                   headers=headers)

        self.assertEqual(sol_ping.status_code, 200)
