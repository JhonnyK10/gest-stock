from sqlalchemy import Column, Integer, String
from src.config.data_base import Base
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    celular = Column(String, unique=True, index=True)
    senha = Column(String)
    status = Column(String, default="Inativo")
    activation_code = Column(String, nullable=True)  # Adicionando campo para o código de ativação

    def __init__(self, nome, cnpj, email, celular, senha, status="Inativo", activation_code=None):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.celular = celular
        self.senha = generate_password_hash(senha)  # Hash da senha
        self.status = status
        self.activation_code = activation_code

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "email": self.email,
            "celular": self.celular,
            "status": self.status,
            "activation_code": self.activation_code
        }
