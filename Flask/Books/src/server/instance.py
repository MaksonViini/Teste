from flask import Flask, blueprints
from flask_restx import Api

app = Flask(__name__)


class Server():
    def __init__(self, ) -> None:
        self.app = Flask(__name__)
        self.blueprint = blueprints('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/docs', title='Api Flask-SQLAlchemy',
                       version='1.0', description='API for the server')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/orm_timescale'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.book_name_space = self.book_name_space()

    def book_name_space(self):
        return self.api.namespace('book', description='Book operations', path='/')

    def run(self, ):
        self.app.run(debug=True, host='0.0.0.0', port=5000)

server = Server()
