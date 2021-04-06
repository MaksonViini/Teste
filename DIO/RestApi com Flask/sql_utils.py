from sql_models import Pessoas


def insere_pessoas():
    # Insere dados na tabela pessoas
    pessoa = Pessoas(nome='Vinicio', idade=20)
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


if __name__ == '__main__':
    # insere_pessoas()
    # consulta()
    # altera_pessoa()
    exclui_pessoa()
    consulta()
