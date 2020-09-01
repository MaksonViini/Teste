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