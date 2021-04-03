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

# Devolve uma desenvolvedor pelo ID, altera e deleta


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = dev[id]
            return jsonify(
                response
            )
        except IndexError:
            response = {
                'status': 'erro',
                'Mensagem': f'Desenvolvedor de ID {id} nao existe'
            }
        except Exception:
            response = {
                'status': 'erro',
                'Mensagem': f'Erro desconhecido, procure o adm da API'
            }
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dev[id] = dados
        return jsonify(
            dados
        )

    elif request.method == 'DELETE':
        dev.pop(id)
        return jsonify(
            {
                'status': 'Sucess',
                'Mensagem': 'Registro excluido!'
            }
        )

# Lista todos os desenvolvedores e permite registrar um novo dev


@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        dev.append(dados)
        return jsonify(
            {
                'status': 'Sucess',
                'Mensagem': 'Registro Inserido!'
            }
        )


if __name__ == '__main__':
    app.run()
