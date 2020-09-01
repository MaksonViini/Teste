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

hist(viagens$Valor.passagens)

# Valores max, min e media .... da coluna valor
summary(viagens$Valor.passagens)

# Visualizando os valores em boxplot
boxplot(viagens$Valor.passagens)

# Desvio padrao
sd(viagens$Valor.passagens)

# Verificar valores nulos nas colunas
colSums(is.na(viagens))

# Verificando ocorrencias

str(viagens$Situação)

# Verificando a quantidade de ocorrencias a cada classe
table(viagens$Situação)

# Valor em percentual
prop.table(table(viagens$Situação)) * 100

# 1 - Quais orgaos estao gastando mais com viagens?
# Criando um dataframe com os 15 que mais gastam
p1 = viagens %>% group_by(Nome.do.órgão.superior) %>% summarise(n = sum(Valor.passagens)) %>% arrange(desc(n)) %>% top_n(15)
names(p1) = c('Orgao', 'Valor')
head(p1)

# Criando grafico de barras com ggplot
library(ggplot2)
ggplot(p1, aes(x=reorder(Orgao, Valor), y=Valor)) + geom_bar(stat='identity') + coord_flip() + labs(x='Valor', y='Orgao')

# Quantidade de gastos por cidades com viagens
p2 = viagens %>% group_by(Destinos) %>% summarise(n=sum(Valor.passagens)) %>% arrange(desc(n)) %>% top_n(15)
names(p2) = c('Destino', 'Valor')
head(p2)

ggplot(p2, aes(x=reorder(Destino, Valor), y=Valor)) + geom_bar(stat='identity', fill='#0ba791') + geom_text(aes(label=Valor), 
vjust=0.3, size=3) + coord_flip() + labs(x='Valor', y='Destino')

options(scipen=999)

# Quantidades de viagens realizadas pro mes
p3 = viagens %>% group_by(data.inicio.formatada) %>% summarise(qtd=n_distinct(Identificador.do.processo.de.viagem))
head(p3)

ggplot(p3, aes(x=data.inicio.formatada, y=qtd, group=1)) + geom_line() + geom_point()


# Visualizacao dos dados com Markdown
install.packages('rmarkdown')
install.packages('tinytex')

tinytex::install_tinytex()