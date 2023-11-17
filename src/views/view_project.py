import os
import requests
from flask_restful import Resource
from flask import request

path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'

path_project = os.getenv('PROJECT_PATH', 'localhost:3003') if os.environ.get(
    'PROJECT_PATH') != 'default' else 'localhost:3003'


class VistaProject(Resource):

    def post(self):
        # Crea un proyecto para una empresa: POST /abcjobs/company/project
        try:
            project = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:

                if response['type'] != '2':
                    return {'error': 'El usuario no es una empresa'}, 400

                idUser = response['id']
                responsePersonal = requests.post(
                    f'http://{path_project}/project/{idUser}', json=project, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self):
        # Obtiene los proyectos de una empresa: GET /abcjobs/company/project
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                idUser = response['id']
                responsePersonal = requests.get(
                    f'http://{path_project}/project/{idUser}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaAspiranteProyecto(Resource):

    def post(self, idProject):
        # Agrega un aspirante a un proyecto: POST /abcjobs/company/project/<int:idProject>
        try:
            aspirant = request.get_json()
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                # TODO: Validar que el usuario sea el dueño del proyecto, falta el GET para obtener un proyecto
                if response['type'] != '2':
                    return {'error': 'El usuario no es una empresa'}, 400

                responsePersonal = requests.post(
                    f'http://{path_project}/project/aspirant/{idProject}', json=aspirant, headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400

    def get(self, idProject):
        # Obtiene los aspirantes e información de un proyecto: GET /abcjobs/company/project/<int:idProject>
        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            if content.status_code == 200:
                # TODO: Validar que el usuario sea el dueño del proyecto, falta el GET para obtener un proyecto
                if response['type'] != '2':
                    return {'error': 'El usuario no es una empresa'}, 400

                responsePersonal = requests.get(
                    f'http://{path_project}/project/aspirant/{idProject}', headers={'Content-Type': 'application/json'})

                return responsePersonal.json(), responsePersonal.status_code

            else:
                return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400
