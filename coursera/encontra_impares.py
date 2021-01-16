def encontra_impares(lista):
    if len(lista) == 0:
        return []
    e = lista.pop(0)
    if e % 2 != 0:
        return [e] + encontra_impares(lista)
    return encontra_impares(lista)


lista = [1, 2, 3, 4]

print(encontra_impares(lista))