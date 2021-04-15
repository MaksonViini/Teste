def menor_strings(str):
    maior = 0
    for i in range(len(str)):
        maior = len(str[i])
        if maior >= len(str[i]):
            maior = len(str[i])
            palavra = str[i].strip()
    return palavra.capitalize()


def mostActive(customers):
    # Write your code here
    lista = customers
    for i in range(len(lista)):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                del(lista[j])
            else:
                j = j + 1
    return sorted(lista)


def minTime(files, numCores, limit):
    files.sort()
    files1 = set(files)
    num1 = sum(files1)
    num2 = files[-limit]
    soma = num1 - num2
    return int((num2 / numCores) + soma)


str = ["Isso", "coisa", "boa", "va"]
print(menor_strings(str))
print(float("3.5") + 5)
print('7-4')
frase = " Python É Uma Linguagem Poderosa "
print(frase.capitalize())

customers = ["isso", "isso", "coisa", "boa", "va", 'coisa']
result = mostActive(customers)
print(result)

#print(minTime([4, 1, 3, 2, 8], 4, 1))
result = minTime([4, 1, 3, 2, 8, 4, 2], 4, 1)
print(result)
