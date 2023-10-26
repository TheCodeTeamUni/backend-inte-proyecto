from src import create_app
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.views import VistaSignUp, VistaLogin, VistaValidate, VistaPong, VistaAspirantes

application = create_app('default')
app_context = application.app_context()
app_context.push()

cors = CORS(application)

api = Api(application)
api.add_resource(VistaAspirantes, '/abcjobs/aspirantes/personal')
api.add_resource(VistaValidate, '/abcjobs/validate')
api.add_resource(VistaSignUp, '/abcjobs/signup')
api.add_resource(VistaLogin, '/abcjobs/login')
api.add_resource(VistaPong, '/')

jwt = JWTManager(application)


@application.errorhandler(404)
def page_not_found(e):
    return 'Pagina no encontrada', 404


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)
