from unittest import TestCase
from faker import Faker
from unittest.mock import patch
from application import application as app


class TestAspirant(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    @patch('src.views.view_aspirant.requests.get')
    def test_post_personal_information(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        new_personal = {
            "name": self.data_factory.name(),
            "lastName": self.data_factory.last_name(),
            "typeDocument": self.data_factory.random_element(elements=('CC', 'TI', 'CE')),
            "document": self.data_factory.ssn(),
            "gender": self.data_factory.random_element(elements=('M', 'F', 'O')),
            "alterntiveEmail": self.data_factory.email(),
            "telephone": self.data_factory.phone_number(),
            "country": self.data_factory.country(),
            "address": self.data_factory.address(),
            "birthdate": '13/05/1992',
            "description": self.data_factory.text(),
            "photo": self.data_factory.image_url()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/aspirantes/personal', json=new_personal, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_personal_information_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_personal = {
            "name": self.data_factory.name(),
            "lastName": self.data_factory.last_name(),
            "typeDocument": self.data_factory.random_element(elements=('CC', 'TI', 'CE')),
            "document": self.data_factory.ssn(),
            "gender": self.data_factory.random_element(elements=('M', 'F', 'O')),
            "alterntiveEmail": self.data_factory.email(),
            "telephone": self.data_factory.phone_number(),
            "country": self.data_factory.country(),
            "address": self.data_factory.address(),
            "birthdate": '13/05/1992',
            "description": self.data_factory.text(),
            "photo": self.data_factory.image_url()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/aspirantes/personal', json=new_personal, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_personal_information(self, mock_get):

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
            '/abcjobs/aspirantes/personal', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_personal_information_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/aspirantes/personal', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_work_experience(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        new_work = {
            "company": self.data_factory.company(),
            "position": self.data_factory.job(),
            "actualJob": False,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/aspirantes/workexperience', json=new_work, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_work_experience_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_work = {
            "company": self.data_factory.company(),
            "position": self.data_factory.job(),
            "actualJob": False,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/aspirantes/workexperience', json=new_work, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_work_experience(self, mock_get):

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
            '/abcjobs/aspirantes/workexperience', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_work_experience_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/aspirantes/workexperience', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_education(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        new_education = {
            "typeEducation": 'Formal',
            "level": 'Maestria',
            "title": self.data_factory.job(),
            "institution": self.data_factory.company(),
            "grade": True,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/aspirantes/education', json=new_education, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_education_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_education = {
            "typeEducation": 'Formal',
            "level": 'Maestria',
            "title": self.data_factory.job(),
            "institution": self.data_factory.company(),
            "grade": True,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/aspirantes/education', json=new_education, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_education(self, mock_get):

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
            '/abcjobs/aspirantes/education', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_education_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/aspirantes/education', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_skill(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 1,
            "username": "UsuarioPrueba0",
            "email": "usuarioprueba0@mail.com",
            "type": "1"
        }

        new_skill = {
            "skill": self.data_factory.job(),
            "level": self.data_factory.text(),
            "experience": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/abcjobs/aspirantes/skill', json=new_skill, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_post_skill_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        new_skill = {
            "skill": self.data_factory.job(),
            "level": self.data_factory.text(),
            "experience": self.data_factory.text()
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.post('/abcjobs/aspirantes/skill', json=new_skill, headers={
                                    'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_skill(self, mock_get):

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
            '/abcjobs/aspirantes/skill', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_skill_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/aspirantes/skill', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_aspirants(self, mock_get):

        token = "miToken"

        user_data = {
            "id": 2,
            "username": "CompanyPrueba0",
            "email": "companyprueba0@mail.com",
            "type": "2"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 200

        response = self.client.get(
            '/abcjobs/aspirantes', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 200)

    @patch('src.views.view_aspirant.requests.get')
    def test_get_aspitants_fail(self, mock_get):

        token = "miToken"

        user_data = {
            "error": "Error"
        }

        mock_get.return_value.json.return_value = user_data
        mock_get.return_value.status_code = 400

        response = self.client.get(
            '/abcjobs/aspirantes', headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(response.status_code, 400)
