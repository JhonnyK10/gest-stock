from src.Infrastructure.Model.user_model import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(name, email, password,cnpj, phone):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            raise ValueError("O email já está cadastrado.")

        user = User(
            name=name,
            email=email,
            password=password,
            cnpj=cnpj,
            phone=phone
        )

        db.session.add(user)
        db.session.commit()
        return user
