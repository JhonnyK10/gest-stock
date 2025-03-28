from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response


def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({ 
            "mensagem": "API - OK",
        }), 200)
    
    @app.route('/new_user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/list_users',methods=['GET'])
    def get_users():
        return UserController.get_users()
    
    @app.route('/active_user',methods=['POST'])
    def active_user():
        return UserController.active_user()
    
    @app.route("/delete_user/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        return UserController.delete_user(user_id)
    
    @app.route("/update_user/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        return UserController.update_user(user_id)
    
    @app.route('/login', methods=['POST'])
    def login():
        return UserController.login_user()