minha_matriz = [[1], [2], [3]]
def dimensoes(matriz):
    tam_matriz = (len(matriz), len(matriz[0]))
    print('{}X{}'.format(tam_matriz[0], tam_matriz[1]))

dimensoes(minha_matriz)