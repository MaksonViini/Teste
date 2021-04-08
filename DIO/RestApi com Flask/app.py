from flask import Flask, request, request
from flask_restful import Resource, Api
import json
from sql_models import Pessoas, Atividades
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'Makson': '123',
#     'Vinicio': '321'
# }


# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha


class Pessoa(Resource):
    @auth.login_required
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
    @auth.login_required
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
    def get(self, nome):
        atividades = Atividades.query.all()
        data = request.json
        if nome == data['pessoa']:
            return [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome}
                    for i in atividades]
        else:
            return {'Status': 'Pessoa nao encontrada!'}

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
api.add_resource(ListaAtividades, '/atividades/<string:nome>/')

if __name__ == '__main__':
    app.run()
