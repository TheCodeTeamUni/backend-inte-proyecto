import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_test = os.getenv('PROJECT_PATH', 'localhost:3003') if os.environ.get(
    'PROJECT_PATH') != 'default' else 'localhost:3003'


class VistaTest(Resource):

    def post(self):
        # Crea una prueba técnica para un aspirante: POST /abcjobs/company/test
        try:
            test = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'Usuario no autorizado'}, 401

                idCompany = response['id']
                responsePersonal = requests.post(
                    f'http://{path_test}/test/company/{idCompany}', json=test, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene las pruebas técnicas de una empresa: GET /abcjobs/company/test
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'Usuario no autorizado'}, 401

                idCompany = response['id']
                responsePersonal = requests.get(
                    f'http://{path_test}/test/company/{idCompany}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaTestAspirant(Resource):

    def get(self):
        # Obtiene las pruebas técnicas de un aspirante: GET /abcjobs/aspirant/test
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '1':
                    return {'error': 'Usuario no autorizado'}, 401

                idAspirant = response['id']
                responsePersonal = requests.get(
                    f'http://{path_test}/test/aspirant/{idAspirant}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
