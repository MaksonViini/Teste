dados = []
with open('Python\Manipulando_arquivos\iris.data', 'r') as iris:
    for registro in iris.readlines():
        dados.append(registro.split(','))

#print(dados)

print(dados[0][1])
