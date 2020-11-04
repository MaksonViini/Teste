curso = c("Eng. Computacao", "Eng. Software", "Sistemas de informacao", "TADS")
aprovado = c(1751, 2186, 947, 200)
reprovado = c(2528, 2132, 1843, 200)


# Primeiro parametro e o eixo Y, segundo argumento e curso
# main titulo do grafico
# lab sao nomes por eixo
barplot(aprovado, names.arg = curso, main = "Aprovado por curso", xlab = "Cursos", 
        ylab = "Aprovado")


# Sub-Titulo
barplot(aprovado, names.arg = curso, main = "Aprovado por curso", xlab = "Cursos", 
        ylab = "Aprovado", sub = "Subtitulo")

# Alterando tamanho do titulo