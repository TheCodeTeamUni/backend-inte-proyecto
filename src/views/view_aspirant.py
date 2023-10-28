import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_aspirant = os.getenv('ASPIRANTS_PATH', 'localhost:3002') if os.environ.get(
    'ASPIRANTS_PATH') != 'default' else 'localhost:3002'


class VistaAspirantes(Resource):

    def post(self):
        # Crea un aspirante en la aplicación: /abcjobs/aspirantes/personal
        try:
            personal = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                personal['idUser'] = response['id']
                responsePersonal = requests.post(
                    f'http://{path_aspirant}/aspirant/personal', json=personal, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaWorkExperience(Resource):

    def post(self):
        # Crea un aspirante en la aplicación: /abcjobs/aspirantes/workexperience
        try:
            work = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                work['idUser'] = response['id']
                responseWork = requests.post(
                    f'http://{path_aspirant}/aspirant/work', json=work, headers={'Content-Type': 'application/json'})

                return responseWork.json(), responseWork.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
