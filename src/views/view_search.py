import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_aspirant = os.getenv('ASPIRANTS_PATH', 'localhost:3002') if os.environ.get(
    'ASPIRANTS_PATH') != 'default' else 'localhost:3002'


class VistaSearchSkill(Resource):

    def get(self, Skill):
        # Obtiene los aspirantes que coincidan con una habilidad: GET /abcjobs/search/<string:Skill>
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response["type"] == "2":
                    response = requests.get(
                        f'http://{path_aspirant}/aspirant/{Skill}', headers={'Content-Type': 'application/json'})

                    return response.json(), response.status_code

                else:
                    return {'error': 'No tiene permisos para realizar esta acción'}, 401

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaSearchAspirant(Resource):

    def get(self, idUser):
        # Obtiene la información personal de un aspirante: GET /abcjobs/search/aspirant/int:idUser>

        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response["type"] == "2":
                    response = requests.get(
                        f'http://{path_aspirant}/aspirant/{idUser}', headers={'Content-Type': 'application/json'})

                    return response.json(), response.status_code

                else:
                    return {'error': 'No tiene permisos para realizar esta acción'}, 401

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
