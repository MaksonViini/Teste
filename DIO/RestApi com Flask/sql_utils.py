from sql_models import Pessoas, Usuarios


def insere_pessoas():
    # Insere dados na tabela pessoas
    pessoa = Pessoas(nome='Makson', idade=20)
    print(pessoa)
    pessoa.save()


def consulta():
    # Realiza Consulta na tabela pessoas
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Makson').first()
    print(pessoas.idade)


def altera_pessoa():
    # Altera dados na tabela pessoas
    pessoa = Pessoas.query.filter_by(nome='Makson').first()
    pessoa.nome = 'Makson Vinicio'
    pessoa.idade = 21
    pessoa.save()


def exclui_pessoa():
    # Exlui dados na tabela pessoas
    pessoa = Pessoas.query.filter_by(nome='Vinicio').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_pessoas()
    # consulta()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta()
    insere_usuario('Makson', '1234')
    insere_usuario('Vinicio', '1234')
    insere_usuario('MaksonViini', '1234')
    consulta_todos_usuarios()
