from sql_models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Vinicio', idade=20)
    print(pessoa)
    pessoa.save()



def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Makson').first()
    print(pessoa.idade)


if __name__ == '__main__':
    # insere_pessoas()
    consulta()
