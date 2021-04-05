from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = dev[id]
            return response
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
        return response

    def put(self, id):
        dados = json.loads(request.data)
        dev[id] = dados
        return dados

    def delete(self, id):
        dev.pop(id)
        return (
            {
                'status': 'Sucess',
                'Mensagem': 'Registro excluido!'
            }
        )


api.add_resource(Desenvolvedor, '/dev/<int:id>/')

if __name__ == '__main__':
    app.run()
