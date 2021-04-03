from flask import Flask, jsonify
from flask.globals import request
import json

app = Flask(__name__)

dev = [{
    'id': '0',
    'Nome': 'Makson',
    'Habilidades': ['Python', 'Ciencia de dados']
},
    {
    'id': '1',
    'Nome': 'Vinicio',
    'Habilidades': ['Python', 'Git']
}]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    '''
    Devolve uma desenvolvedor pelo ID, altera e deleta
    '''
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


@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    ''' 
    Lista todos os desenvolvedores e permite registrar um novo dev
    '''
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(dev)
        dados['id'] = posicao
        dev.append(dados)
        return jsonify(
            dev[posicao]
        )
    elif request.method == 'GET':
        return jsonify(dev)


if __name__ == '__main__':
    app.run()
