# Carregando os dados
viagens = read.csv(file = 'C:/Users/Makson/Documents/GitHub/Teste/2020_Viagem.csv', sep = ';', dec = ',')
head(viagens)
View(viagens)
dim(viagens)

summary(viagens)
summary(viagens$valor.passagens)

# Verificando o tipo de dados
library(dplyr)
glimpse(viagens)

# Converter para o tipo data
viagens$data.inicio = as.Date(viagens$Período...Data.de.início, '%d/ %m/ %y')
glimpse(viagens)

# Formatando o campo data para trabalhar apenas com mes e ano
viagens$data.inicio.formatada = format(viagens$data.inicio, '%Y-%m')
head(viagens$data.inicio.formatada)

# Explorando os dados

hist(viagens$valor.passagens)

# Valores max, min e media .... da coluna valor
summary(viagens$valor.passagens)

# Visualizando os valores em boxplot
boxplot(viagens$valor.passagens)

# Desvio padrao

sd(viagens$valor.passagens)