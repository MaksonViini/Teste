from flask import Flask, jsonify, request
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
    doc='/docs/'
)

data = {
    'id': 1,
    'value': 10
}

class Model(Resource):
    def get(self):
        return jsonify(data)

    def post(self):
        data['id'] = request.json['id']
        data['value'] = request.json['value']
        return jsonify(data)

api.add_resource(Model, '/model/')

if __name__ == '__main__':
    app.run(debug=True)
