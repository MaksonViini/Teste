lista = [1,2,1,3,4,7,10]
def remove_repetidos(lista):
    lista1 = [i for i in set(lista)]

    return sorted(lista1)

print(remove_repetidos(lista))