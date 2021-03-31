lista = [1, 10]

try:
    divisao = 10 / 1
    numero = lista[1]
    # x = a

except ZeroDivisionError:
    print('Nao e possivel realizar uma divisao por 0')

except IndexError:
    print('Erro de Indice')

except Exception as ex:
    print('Erro desconhecido: Erro {}'.format(ex))

else:
    print('Nao ocorreu nenhuma excecao!!!')

finally:
    print('Sempre executa')