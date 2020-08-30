msg = 'Hello world'
print(msg)
# Install pacotes
install.packages('ggplot2')
# Importando pacotes
library(ggplot2)

# Vetores
cidade = c('Brasilia', 'SP', 'MG', 'RJ')
cidade
temperatura = c('32, 22, 18, 30')
regiao = c('1, 2, 2, 2')

# Acessando o elemento do vetor
cidade[1]
# Intervalo de valores
cidade[1:3]
#Copiando um vetor
cidade2 = cidade
cidade2
# Excluindo o segundo elemento da consulta
cidade2[-2]
# Alterando um vetor
cidade2[3] = 'Belo Horizonte'
cidade2
# Adicionando um novo elemento 
cidade2[5] = 'Curitiba'

# Deletar um vetor
cidade = NULL
cidade


# Fatores
uf = factor(c('DF', 'BH', 'RJ', 'SP'))
uf

#grau_instrucao = factor(c('Nivel medio', 'Superior', 'Nivel medio', 'Fundamental'), Levels = c('Fundamental', 'Medio', 'Superior'), 
#ordered = TRUE)

# lista

pessoa = list(sexo = 'M', cidade = 'BH', idade = '20')
pessoa

# Acessando o primeiro elemento da lista
pessoa[1]
# Acessando o valor do terceiro elemento
pessoa[[3]]

# Editando uma lista
pessoa[['idade'] = 30
pessoa

# Filtrando elementos de uma lista
pessoa[c('cidade', 'idade')]

# Criando um dataframe com vetores

df = data.frame(cidade2, temperatura)
df

# Criando um dataframe com listas

df2 = data.frame(cidade2)
df2

#Filtrando o dataframe
# Recuperando o valor da linha 1 e coluna 2
df[1, 2]

# Todas as linhas da primeira coluna
df[, 1]

# Primeira linha e todas as colunas
df[1, ]

# Selecionando as 3 primeiras linhas 
# Da primeira e ultima coluna
df2[c(1:2), c(1:2)]

# Verificando nome das colunas
names(df)

# Verificando numero de linhas x colunas
dim(df)

# Verificando os tipos de dados
str(df)

# Acessando dados de uma coluna
df['cidade2']

# Matrizes
m = matrix(seq(1:9), nrow = 3)
m

m2 = matrix(seq(1:25), ncol=5, byrow=TRUE, dimnames = list(c(seq(1:5)), c('A', 'B', 'C', 'D', 'E')))
m2

# Filtrando matriz

m2[c(1:3), c(1:3)]

### Funcao for
for(i in seq(1:20)) {
    print(i)
}

# While
i = 0
while(i <= 10) {
    print(i)
    i = i + 1
}

# Condicional if
i = 4
if (i <= 4) {
    print(i)
}
x = 4
y = 2
ifelse(x > y, "X e maior", "Z e maior")

# Funcoes
par.impar = function() {
    for(i in seq(1:20)){
        if((i %% 2) == 0) {
            print(i)
        } else 
            print(' ')
    }
}
par.impar()

# Funcao Apply
x = seq(1:9)
matriz = matrix(x, ncol=3)
matriz
result1 = apply(matriz, 1, sum) # 1 Para linha 2 para coluna
result1

result2 = apply(matriz, 2, sum) # 1 Para linha 2 para coluna
result2

# Funcao lapply
numeros.i = c(1, 3, 5, 7, 9, 11, 13, 15)
numeros.p = c(2, 4, 6, 8, 10, 12, 14, 16)
numeros = list(numeros.i, numeros.p)
numeros
lapply(numeros, mean)
sapply(numeros, mean)

# Graficos
mtcars
carros = mtcars[c(1, 2, 9)]
head(carros)

# Criando histogramas
hist(carros$mpg)

# Grafico de dispersao
plot(carros$mpg, carros$cyl)

# Graficos usando ggplot2
library(ggplot2)

ggplot(carros, aes(am)) + geom_bar()

# Utilizando JOIN
install.packages("dplyr")
library(dplyr)
df1 = data.frame(produto = c('Lapis', 'Caneta', 'Papel'), preco = c(1.2, 1.8, 3))
head(df1)
df2 = data.frame(produto = c(1, 2, 3), nome = c('A', 'B', 'C'))
head(df2)

df3 = left_join(df1, df2, 'produto')
head(df3)

df4 = right_join(df1, df2, 'produto')

df5 = inner_join(df1, df2, 'produto')


# DPLYR
iris
head(iris)

glimpse(iris) # Informacoes do dataset

# Filter - filtrando os dados - apenas versicolor
versicolor = filter(iris, Species == 'versicolor')
dim(versicolor)

# Slice - selecionando algumas linhas especificas
slice(iris, 5:10)

# Select - selecionando algumas linhas
head(select(iris, 2:4))

# Todas as colunas exceto Sepal.Width
head(select(iris, -Sepal.Width))


# Criando uma nova coluna com base em colunas existentes 
iris2 = mutate(iris, nova.coluna = Sepal.Length + Sepal.Width)
head(iris2)

head(iris2[, c('Sepal.Length', 'Sepal.Width', 'nova.coluna')])

# ORDENAR
arrange
select(iris, Sepal.Length) %>% arrange(Sepal.Length)  # %>% Executar mais de uma operacao

# Group by

iris %>% group_by(Species) %>% summarise(mean(Sepal.Length))

# 3.3 Transformando os dados





