from flask.wrappers import Response
from flask import Flask, request, request
from flask_restful import Resource, Api
import json
from sql_models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            return {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            return {
                'Status': 'Erro',
                'Mensagem': 'Pessoa nao encontrada!'
            }

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        return {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        msg = f'Pessoa {pessoa.nome} excluida com sucesso!'
        pessoa.delete()
        return {
            'Status': 'Sucesso',
            'Mensagem': msg
        }


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        return [{'id': i.id, 'nome': i.nome, 'idade': i.idade}
                for i in pessoas]

    def post(self):
        data = request.json
        pessoa = Pessoas(nome=data['nome'], idade=data['idade'])
        pessoa.save()
        return {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        return [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome}
                for i in atividades]

    def post(self):
        data = request.json
        pessoa = Pessoas.query.filter_by(nome=data['pessoa']).first()
        atividade = Atividades(nome=data['nome'], pessoa=pessoa)
        atividade.save()
        return {
            'id': atividade.id,
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome
        }


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run()
