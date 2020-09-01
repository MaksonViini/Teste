# Carregando os dados
diabetes = read.csv(file = 'C:/Users/Makson/Documents/GitHub/Teste/diabetes.csv')
head(diabetes)

# Preparacao dos dados
str(diabetes)

# Verificando NaN
colSums(is.na(diabetes))

# Explorando os dados
diabetes$Outcome = as.factor(diabetes$Outcome)

summary(diabetes$Insulin) # Media, Mediana, Min e Max
boxplot(diabetes$Insulin) #bloxplot

# Analise exploratoria
boxplot(diabetes)

hist(diabetes$Pregnancies)
hist(diabetes$Age)
hist(diabetes$BMI)

library(dplyr)
diabetes2 = diabetes %>% filter(Insulin <= 250)
boxplot(diabetes2$Insulin)

# Construcao do modelo
install.packages('caTools')
library(caTools) # Pacote para dividir entre treino e teste

set.seed(123)
index = sample.split(diabetes2$Pregnancies, SplitRatio = .70) # Dividindo o pacote entre treino e teste
index

# Criando novos conjuntos de dados Train e Test
train = subset(diabetes2, index == TRUE)
test = subset(diabetes2, index == FALSE)

# Verificando as dimensoes dos datasets
dim(diabetes2)
dim(train)
dim(test)

# Instalando pacote para criacao do modelo
install.packages('caret')
install.packages('e1071')

# Carregando os pacotes
library(caret)
library(e1071)

modelo = train(Outcome ~., data = train, method = 'knn')
