from flask import Flask, Blueprint
from flask_restx import Api
from mashmallow import ma
from database import db


class Server():
    def __init__(self, ) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/docs', title='Api Flask-SQLAlchemy',
                       version='1.0', description='API for the server')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@172.22.0.1:3306/orm_timescale1"'
        # 'sqlite:///data.db'
        # 'postgresql://postgres:postgres@localhost:5432/orm_timescale'
        # "postgresql://postgres:postgres@172.22.0.1:3306/orm_timescale1"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.book_name_space = self.book_name_space()

    def book_name_space(self):
        return self.api.namespace('book', description='Book operations', path='/')

    def run(self, ):
        self.app.run(debug=True)


server = Server()
