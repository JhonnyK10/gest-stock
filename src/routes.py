from flask import jsonify, make_response, Blueprint
from src.Application.Controllers.user_controller import UserController

# Criação do Blueprint para as rotas de usuário
user_blueprint = Blueprint('user', __name__)

# Definição das rotas relacionadas ao usuário
user_blueprint.route('/register', methods=['POST'])(UserController.register_user)
user_blueprint.route('/activate', methods=['POST'])(UserController.activate_user)
user_blueprint.route('/login', methods=['POST'])(UserController.login_user)

def init_routes(app):
    # Rota de health check
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK",
        }), 200)

    # Registra o Blueprint de usuário na aplicação
    app.register_blueprint(user_blueprint, url_prefix='/user')
    
    

