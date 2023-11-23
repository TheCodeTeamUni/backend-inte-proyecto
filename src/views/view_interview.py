import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_interview = os.getenv('PROJECT_PATH', 'localhost:3003') if os.environ.get(
    'PROJECT_PATH') != 'default' else 'localhost:3003'


class VistaInterview(Resource):

    def post(self):
        # Crea una entrevista para un proyecto: POST /abcjobs/company/interview
        try:
            interview = request.get_json()
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
                    f'http://{path_interview}/interview/company/{idCompany}', json=interview, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene las entrevistas de una empresa: GET /abcjobs/company/interview
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
                    f'http://{path_interview}/interview/company/{idCompany}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaInterviewAspirant(Resource):

    def get(self):
        # Obtiene las entrevistas de un aspirante: GET /abcjobs/aspirant/interview
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idAspirant = response['id']
                responsePersonal = requests.get(
                    f'http://{path_interview}/interview/aspirant/{idAspirant}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaInterviewDetail(Resource):

    def get(self, idInterview):
        # Obtiene el detalle de una entrevista: GET /abcjobs/interview/<int:idInterview>
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                #TODO: Validar que el usuario sea el aspirante a entrevistar

                responsePersonal = requests.get(
                    f'http://{path_interview}/interview/{idInterview}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaInterviewResult(Resource):

    def post(self, idInterview):
        # Crea el resultado de una entrevista: POST /abcjobs/interview/result/<int:idInterview>

        try:
            result = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'Usuario no autorizado'}, 401

                responsePersonal = requests.post(
                    f'http://{path_interview}/interview/result/{idInterview}', json=result, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self, idInterview):
        # Obtiene el resultado de una entrevista: GET /abcjobs/interview/result/<int:idInterview>

        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                responsePersonal = requests.get(
                    f'http://{path_interview}/interview/result/{idInterview}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
