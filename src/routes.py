from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response, Blueprint

user_blueprint = Blueprint('user', __name__)

user_blueprint.route('/register', methods=['POST'])(UserController.register)
user_blueprint.route('/activate', methods=['POST'])(UserController.activate)
user_blueprint.route('/login', methods=['POST'])(UserController.login)

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    

