def menor_nome(nomes):
    return min(nomes, key=lambda x: len(x.strip())).capitalize().strip()


print(menor_nome(['maria', ' josé ', '   PAULO', 'Catarina   ']))
