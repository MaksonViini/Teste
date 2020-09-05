library(ggplot2)
Is = 2.682000E-09
Vd = 7.18E-01 
Id = 9.28E-03
k = 11600
T = 273

Id = Is * (k*Vd / exp(T*k) - 1)
print(Id)

ggplot(Id + geom_bar())