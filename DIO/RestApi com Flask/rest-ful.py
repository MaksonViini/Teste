from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilitadades import Habilidades


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
    '''
    Devolve uma desenvolvedor pelo ID, altera e deleta
    '''

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


class ListaDesenvolvedores(Resource):
    '''
    Devolve uma listagem dos desenvolvedores e inclui algum dev
    '''

    def get(self):
        return dev

    def post(self):
        dados = json.loads(request.data)
        posicao = len(dev)
        dados['id'] = posicao
        dev.append(dados)
        return dev[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run()
