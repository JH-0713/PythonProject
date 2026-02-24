# importar as Bibliotecas
from flask_login import UserMixin
from sqlalchemy import create_engine, String, Integer, func, Column, DateTime, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash

# Base de Dados
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/empresa_db')


db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Funcionarios(Base, UserMixin):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String,nullable=False)
    data_nascimento = Column(String(50),nullable=False)
    cpf = Column(String(11),nullable=False)
    email = Column(String,nullable=False, unique=True)
    senha = Column(String,nullable=False, unique=True)
    cargo = Column(String(50),nullable=False)
    salario = Column(Float,nullable=False)

    def __repr__(self):
        return f'<Funcionarios: {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            print(F'Error: {SQLAlchemyError}')
            db_session.rollback()
            raise
        except Exception:
            print(f'Error_: {Exception}')
            db_session.rollback()
            raise
