from src import create_app
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.views import VistaSignUp, VistaLogin, VistaValidate, VistaPong, VistaMe
from src.views import VistaPersonalInformation, VistaWorkExperience, VistaEducation, VistaSkill, VistaAspirantes
from src.views import VistaProject, VistaAspiranteProyecto
from src.views import VistaSearchSkill, VistaSearchAspirant
from src.views import VistaInterview, VistaInterviewAspirant, VistaInterviewDetail, VistaInterviewResult
from src.views import VistaPerformance
from src.views import VistaTest, VistaTestAspirant


application = create_app('default')
app_context = application.app_context()
app_context.push()

cors = CORS(application)

api = Api(application)
api.add_resource(VistaPong, '/')

# Endpoints para aspirantes
api.add_resource(VistaWorkExperience, '/abcjobs/aspirantes/workexperience')
api.add_resource(VistaPersonalInformation, '/abcjobs/aspirantes/personal')
api.add_resource(VistaEducation, '/abcjobs/aspirantes/education')
api.add_resource(VistaSkill, '/abcjobs/aspirantes/skill')
api.add_resource(VistaAspirantes, '/abcjobs/aspirantes')

# Endpoints para proyectos
api.add_resource(VistaAspiranteProyecto,
                 '/abcjobs/company/project/<int:idProject>')
api.add_resource(VistaProject, '/abcjobs/company/project')

# Endpoints para usuarios
api.add_resource(VistaValidate, '/abcjobs/validate')
api.add_resource(VistaSignUp, '/abcjobs/signup')
api.add_resource(VistaLogin, '/abcjobs/login')
api.add_resource(VistaMe, '/abcjobs/me')

# Endpoints para búsqueda
api.add_resource(VistaSearchAspirant, '/abcjobs/search/aspirant/<int:idUser>')
api.add_resource(VistaSearchSkill, '/abcjobs/search/<string:Skill>')

# Endpoints para entrevistas
api.add_resource(VistaInterviewAspirant, '/abcjobs/aspirant/interview')
api.add_resource(VistaInterview, '/abcjobs/company/interview')
api.add_resource(VistaInterviewDetail, '/abcjobs/interview/<int:idInterview>')
api.add_resource(VistaInterviewResult,
                 '/abcjobs/interview/result/<int:idInterview>')


# Endpoints para evaluaciones de desempeño
api.add_resource(VistaPerformance, '/abcjobs/performance/<int:idAspirant>')

# Endpoints para pruebas técnicas
api.add_resource(VistaTest, '/abcjobs/company/test')
api.add_resource(VistaTestAspirant, '/abcjobs/aspirant/test')


jwt = JWTManager(application)


@application.errorhandler(404)
def page_not_found(e):
    return 'Pagina no encontrada', 404


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)
