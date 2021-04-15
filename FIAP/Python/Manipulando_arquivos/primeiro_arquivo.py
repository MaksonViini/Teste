with open('primeiroarquivo.txt', 'r') as arquivo:
    # arquivo.write('Mais codigo no TXT\n')
    conteudo = arquivo.read()
    print(conteudo)
