from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db
from src.Infrastructure.http.whats_app import api_whats_app
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    @staticmethod
    def create_user(name, email, password, cnpj, celular):
        try:
            # Gera o código de ativação via WhatsApp
            activation_code = api_whats_app(celular)  # Assumindo que api_whats_app agora recebe o número de celular

            # Cria o domínio do usuário
            new_user = UserDomain(name, email, password, cnpj, celular)

            # Cria o modelo de usuário para persistência
            user = User(
                name=new_user.name,
                email=new_user.email,
                password=new_user.password,  # Certifique-se de que a senha está sendo hasheada
                cnpj=new_user.cnpj,
                celular=new_user.celular,
                activation_code=activation_code,
                status="Inativo"  # Status padrão
            )

            # Adiciona e commita o usuário no banco de dados
            db.session.add(user)
            db.session.commit()

            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Database error: {str(e)}")
        except Exception as e:
            raise Exception(f"Error creating user: {str(e)}")

    @staticmethod
    def activate_user(email, activation_code):
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                raise Exception("User not found")

            if user.activation_code != activation_code:
                raise Exception("Invalid activation code")

            user.status = "Ativo"
            db.session.commit()

            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Database error: {str(e)}")
        except Exception as e:
            raise Exception(f"Error activating user: {str(e)}")

    @staticmethod
    def authenticate_user(email, password):
        try:
            user = User.query.filter_by(email=email).first()
            if not user or user.password != password:  # Certifique-se de comparar hashes de senha
                raise Exception("Invalid email or password")

            if user.status != "Ativo":
                raise Exception("User not activated")

            # Aqui você pode gerar um token JWT ou OAuth
            return {"message": "User authenticated successfully"}
        except Exception as e:
            raise Exception(f"Error authenticating user: {str(e)}")
