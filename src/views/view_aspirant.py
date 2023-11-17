import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_aspirant = os.getenv('ASPIRANTS_PATH', 'localhost:3002') if os.environ.get(
    'ASPIRANTS_PATH') != 'default' else 'localhost:3002'


class VistaPersonalInformation(Resource):

    def post(self):
        # Crea la información personal de un aspirante: POST /abcjobs/aspirantes/personal
        try:
            personal = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.post(
                    f'http://{path_aspirant}/aspirant/personal/{idUser}', json=personal, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene la información personal del aspirante: GET /abcjobs/aspirantes/personal
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.get(
                    f'http://{path_aspirant}/aspirant/personal/{idUser}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaWorkExperience(Resource):

    def post(self):
        # Crea la informacion laboral del aspirante: POST /abcjobs/aspirantes/workexperience
        try:
            work = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responseWork = requests.post(
                    f'http://{path_aspirant}/aspirant/work/{idUser}', json=work, headers={'Content-Type': 'application/json'})

                return responseWork.json(), responseWork.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene información laboral del aspirante: GET /abcjobs/aspirantes/workexperience
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responseWork = requests.get(
                    f'http://{path_aspirant}/aspirant/work/{idUser}', headers={'Content-Type': 'application/json'})

                return responseWork.json(), responseWork.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaEducation(Resource):

    def post(self):
        # Crea la información academica del aspirante: POST /abcjobs/aspirantes/education
        try:
            education = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.post(
                    f'http://{path_aspirant}/aspirant/education/{idUser}', json=education, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene la información academica del aspirante: GET /abcjobs/aspirantes/education
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.get(
                    f'http://{path_aspirant}/aspirant/education/{idUser}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaSkill(Resource):

    def post(self):
        # Crea habilidades de un aspirante: POST /abcjobs/aspirantes/skill
        try:
            skill = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.post(
                    f'http://{path_aspirant}/aspirant/skill/{idUser}', json=skill, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene habilidades de un aspirante: GET /abcjobs/aspirantes/skill
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.get(
                    f'http://{path_aspirant}/aspirant/skill/{idUser}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaAspirantes(Resource):
    def get(self):
        # Obtiene los aspirantes: GET /abcjobs/aspirantes
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'No esta autorizado para esta acción'}, 400

            response = requests.get(
                f'http://{path_aspirant}/aspirant', headers={'Content-Type': 'application/json'})

            return response.json(), response.status_code

        except Exception as e:
            return {'error': str(e)}, 400
