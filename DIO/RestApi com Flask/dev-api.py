from flask import Flask, jsonify
from flask.globals import request
import json

app = Flask(__name__)

dev = [{
    'Nome': 'Makson',
    'Habilidades': ['Python', 'Ciencia de dados']
},
    {
    'Nome': 'Vinicio',
    'Habilidades': ['Python', 'Git']
}]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def developer(id):
    if request.method == 'GET':
        desenvolvedor = dev[id]
        return jsonify(
            desenvolvedor
        )

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dev[id] = dados
        return jsonify(
            dados
        )


if __name__ == '__main__':
    app.run()
