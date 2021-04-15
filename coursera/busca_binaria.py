def busca(lista, item):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
        print(meio)
    return False


print(busca([1, 2, 3, 4, 5, 6], 4))
