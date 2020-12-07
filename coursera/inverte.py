num = None
lista = []
while num != 0:
    num = int(input('Digite um numero: '))
    lista.append(num)

lista.reverse()
for i in lista:
    if i > 0:
        print(i, end='\n')
