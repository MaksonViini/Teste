def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1

print(busca([12, 13, 14], 15))
# deve devolver => False
