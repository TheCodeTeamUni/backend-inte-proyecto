from src import create_app
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.views import VistaSignUp, VistaLogin, VistaValidate, VistaPong, VistaMe
from src.views import VistaPersonalInformation, VistaWorkExperience, VistaEducation, VistaSkill

application = create_app('default')
app_context = application.app_context()
app_context.push()

cors = CORS(application)

api = Api(application)
api.add_resource(VistaWorkExperience, '/abcjobs/aspirantes/workexperience')
api.add_resource(VistaPersonalInformation, '/abcjobs/aspirantes/personal')
api.add_resource(VistaEducation, '/abcjobs/aspirantes/education')
api.add_resource(VistaSkill, '/abcjobs/aspirantes/skill')
api.add_resource(VistaValidate, '/abcjobs/validate')
api.add_resource(VistaSignUp, '/abcjobs/signup')
api.add_resource(VistaLogin, '/abcjobs/login')
api.add_resource(VistaMe, '/abcjobs/me')
api.add_resource(VistaPong, '/')

jwt = JWTManager(application)


@application.errorhandler(404)
def page_not_found(e):
    return 'Pagina no encontrada', 404


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)
