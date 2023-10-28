from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestUsuario(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_user.requests.post')
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

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_user.requests.post')
    def test_login_successful(self, mock_post):

        login_data = {
            "id": 1,
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "type": "1"
        }

        user_login = {
            "email": self.data_factory.email(),
            "password": self.data_factory.password(),
        }

        mock_post.return_value.json.return_value = login_data
        mock_post.return_value.status_code = 200

        response = self.client.post('/abcjobs/login', json=user_login)

        self.assertEqual(response.json, login_data)
        self.assertEqual(response.status_code, 200)

    def test_login_missing_fields(self):

        user_login = {
            "email": self.data_factory.email(),
        }

        response = self.client.post('/abcjobs/login', json=user_login)

        self.assertEqual(response.json['mensaje'],
                         'Por favor ingresar todos los campos')
        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_user.requests.post')
    def test_validate_email_successful(self, mock_post):

        validate_data = {
            "mensaje": "Usuario no existe"
        }

        email_validate = {
            "email": self.data_factory.email()
        }

        mock_post.return_value.json.return_value = validate_data
        mock_post.return_value.status_code = 200

        response = self.client.post('/abcjobs/validate', json=email_validate)

        self.assertEqual(response.json, validate_data)
        self.assertEqual(response.status_code, 200)

    def test_validate_email_missing_fields(self):

        response = self.client.post('/abcjobs/validate')

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

    @patch('src.views.view_aspirant.requests.get')
    def test_users_me(self, mock_get):

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
            '/abcjobs/me', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, user_data)
