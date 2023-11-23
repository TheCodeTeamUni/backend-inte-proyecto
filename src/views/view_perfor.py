import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_perfor = os.getenv('PROJECT_PATH', 'localhost:3003') if os.environ.get(
    'PROJECT_PATH') != 'default' else 'localhost:3003'


class VistaPerformance(Resource):

    def post(self, idAspirant):
        # Crea una evalucación de desempeño a un aspirante: POST /abcjobs/performance/<int:idAspirant>

        try:
            performance = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'Usuario no autorizado'}, 401

                response = requests.post(
                    f'http://{path_perfor}/performance/{idAspirant}', json=performance, headers={'Content-Type': 'application/json'})

                return response.json(), response.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self, idAspirant):
        # Visualiza el promedio de las evaluaciones de desempeño de un aspirante: GET /abcjobs/performance/<int:idAspirant>

        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                response = requests.get(
                    f'http://{path_perfor}/performance/{idAspirant}', headers={'Content-Type': 'application/json'})

                return response.json(), response.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
