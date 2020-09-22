def soma_matrizes (m1, m2):
    num_lin = len(m1)
    num_col = len(m1[0])
    C = crie_matriz(num_lin, num_col, 0)

    for lin in range(num_lin):
        for col in range(num_col):
            C[lin][col] = m1[lin][col] + m2[lin][col]

    return C


def crie_matriz(n_linhas, n_colunas, valor):
	    matriz = [] # lista vazia
	    for i in range(n_linhas):
	        # cria a linha i
	        linha = [] # lista vazia
	        for j in range(n_colunas):
	            linha.append(valor)
	
	        # coloque linha na matriz
	        matriz.append(linha)
	
	    return matriz


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))