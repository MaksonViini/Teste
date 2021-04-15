def ordenada(lista):
    valor = lista[0]
    for i in range(len(lista)):
        if valor <= lista[i]:
            valor = lista[i]
        else:
            return False
    return True


lista = [1, 5, 8]

print(ordenada(lista))
