from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestInterview(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_test.requests.get')
    def test_post_test(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/company/test', json=data, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_test.requests.get')
    def test_post_test_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/company/test', json=data, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_test.requests.get')
    def test_post_test_unanthorized(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "userPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "1"
        }

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/company/test', json=data, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 401)

    @patch('src.views.view_test.requests.get')
    def test_get_test_company(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/company/test', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_test.requests.get')
    def test_get_test_company_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/company/test', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_test.requests.get')
    def test_get_tests_aspirant(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "userPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "1"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/aspirant/test', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_test.requests.get')
    def test_get_tests_aspirant_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/aspirant/test', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
