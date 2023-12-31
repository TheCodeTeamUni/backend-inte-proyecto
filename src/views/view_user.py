import os
import requests
from flask_restful import Resource
from flask import request


path_user = os.getenv('USERS_PATH', 'localhost:3001') if os.environ.get(
    'USERS_PATH') != 'default' else 'localhost:3001'


class VistaSignUp(Resource):

    def post(self):
        # Crea un usuario en la aplicación: /abcjobs/signup

        try:
            username = request.json['username']
            email = request.json['email']
            userpass = request.json['password']
            type = request.json['type']

            newUser = {
                "username": username,
                "email": email,
                "password": userpass,
                "type": type
            }

            try:
                response = requests.post(
                    f'http://{path_user}/users/signup', json=newUser)

                return response.json(), response.status_code

            except Exception as e:
                return {'mensaje': str(e)}, response.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaLogin(Resource):

    def post(self):
        # Inicia sesión en la aplicación: /abcjobs/login

        try:
            email = request.json['email']
            userpass = request.json['password']

            userLogin = {
                "email": email,
                "password": userpass
            }

            try:
                response = requests.post(
                    f'http://{path_user}/users/login', json=userLogin)

                return response.json(), response.status_code

            except Exception as e:
                return {'mensaje': str(e)}, response.status_code

        except Exception as e:
            return {'mensaje': 'Por favor ingresar todos los campos', 'error': str(e)}, 400


class VistaValidate(Resource):

    def post(self):
        # Valida que el correo ingresado no exista en la aplicación: /abcjobs/validate

        try:
            email = request.json['email']

            userEmail = {
                "email": email
            }

            try:
                response = requests.post(
                    f'http://{path_user}/users/validate', json=userEmail)

                return response.json(), response.status_code

            except Exception as e:
                return {'mensaje': str(e)}, response.status_code

        except Exception as e:
            return {'mensaje': 'Por favor ingresar todos los campos', 'error': str(e)}, 400


class VistaMe(Resource):

    def get(self):
        # Retorna la información del usuario logueado: /abcjobs/me

        try:
            token = request.headers.get('Authorization', None)[7:]
            headers = {'Authorization': 'Bearer {0}'.format(token)}
            content = requests.get(
                f'http://{path_user}/users/me', headers=headers)
            response = content.json()

            return response, content.status_code

        except Exception as e:
            return {'error': str(e)}, 400


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong integrador V3.0', 200
