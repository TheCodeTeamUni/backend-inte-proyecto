from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestInterview(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_aspirant.requests.get')
    def test_post_interview(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        new_interview = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "notes": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/company/interview', json=new_interview, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_interview_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_interview = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "notes": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/company/interview', json=new_interview, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_interviews_company(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/company/interview', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_interviews_company_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/company/interview', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_interviews_aspirant(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "usuarioPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "1"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get('/abcjobs/aspirant/interview', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_interviews_aspirant_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get('/abcjobs/aspirant/interview', headers={
            'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
