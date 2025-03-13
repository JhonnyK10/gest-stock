from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cnpj = data.get('cnpj')  # Adicionando CNPJ
        celular = data.get('celular')  # Adicionando celular

        # Verifica se todos os campos obrigatórios estão presentes
        if not name or not email or not password or not cnpj or not celular:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        try:
            # Cria o usuário usando o UserService
            user = UserService.create_user(name, email, password, cnpj, celular)
            return make_response(jsonify({
                "mensagem": "User salvo com sucesso",
                "usuario": user.to_dict()  # Assumindo que o método to_dict() existe no modelo User
            }), 201)  # Usando 201 para indicar que o recurso foi criado com sucesso
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def activate_user():
        data = request.get_json()
        activation_code = data.get('activation_code')
        email = data.get('email')

        if not activation_code or not email:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        try:
            UserService.activate_user(email, activation_code)
            return make_response(jsonify({"mensagem": "User ativado com sucesso"}), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 400)

    @staticmethod
    def login_user():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        try:
            token = UserService.authenticate_user(email, password)
            return make_response(jsonify({"token": token}), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 401)
