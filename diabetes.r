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

# Criacao do modelo baseado no algoritmo KNN
modelo = train(Outcome ~., data = train, method = 'knn')

# Verificando as metricas
modelo$results
modelo$bestTune

# Testando outros valores de K
modelo2 = train(Outcome ~., data = train, method = 'knn', tuneGrid = expand.grid(k = c(1:20)))
modelo2$results
modelo2$bestTune

plot(modelo2)

# Criando outro modelo
modelo3 = train(Outcome ~., data = train, method = 'naive_bayes')
modelo3$results
modelo3$bestTune

# Testando o modelo SVM
sed.seed(100)
modelo4 = train(Outcome ~., data = train, method = 'svmRadialSigma', preProcess = c('center'))
modelo4$results
modelo3$bestTune

# Avaliando o modelo, predicao
predicoes = predict(modelo4, test)
predicoes

# Comparacao com o conjunto de treino na matriz de confusao
confusionMatrix(predicoes, test$Outcome)

# Realizando predicoes
novos.dados = data.frame(Pregnancies = c(3), 
    Glucose = c(111.50), 
    BloodPressure = c(70), 
    SkinThickness = c(20), 
    Insulin = c(47.09), 
    BMI = c(30.80), 
    DiabetesPedigreeFunction = c(0.34),
    Age = c(28))
novos.dados

# Previsao
previsao = predict(modelo4, novos.dados)
resultado = ifelse(previsao == 1, 'Positivo', 'Negativo')
print(paste('Resultado', resultado))

# Visualizacao dos resultados
write.csv(predicoes, 'resultado.csv')