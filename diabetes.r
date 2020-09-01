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