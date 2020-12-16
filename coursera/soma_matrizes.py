def soma_matrizes(m1, m2):

	tam_matriz = (len(m1), len(m1[0]))
	tam_matriz1 = (len(m2), len(m2[0]))

	if tam_matriz != tam_matriz1:
		return False
	num_lin = tam_matriz[0]
	num_col = tam_matriz[1]
	C = [[0, 0, 0], [0, 0, 0]]
	for lin in range(num_lin):
		for col in range(num_col):
			C[lin][col] = m1[lin][col] + m2[lin][col]

	return C


m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))