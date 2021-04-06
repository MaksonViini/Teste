from flask import Flask, jsonify
from flask.globals import request
import json

app = Flask(__name__)

tarefas = [{
    'id': '0',
    'responsavel': 'Makson',
    'tarefa': 'Desenvolver metodo GET',
    'status': 'Concluido'
},
    {
    'id': '1',
    'responsavel': 'Vinicio',
    'tarefa': 'Desenvolver metodo POST',
    'status': 'Pendente'
}]


@app.route('/task/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def task(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
            return jsonify(response)
        except IndexError:
            response = {
                'status': 'erro',
                'Mensagem': f'A tarefa de ID {id} nao existe'
            }
        except Exception:
            response = {
                'status': 'erro',
                'Mensagem': f'Erro desconhecido, procure o adm da API'
            }
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify(
            {
                'status': 'Sucess',
                'Mensagem': 'Registro excluido!'
            }
        )


@app.route('/task/', methods=['GET', 'POST'])
def lista_task():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id']['status'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run()
