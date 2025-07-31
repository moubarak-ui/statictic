import random
CustomerID = [1, 2, 3, 4, 5]
#prenons 3 échantillons sans remise
print(random.sample(CustomerID, 3))
#[1, 2, 4]
#prenons 3 échantillons avec remise
print(random.choices(CustomerID, k=3))
#[3, 4, 3]
exemple = [1,2,3,4,4,5,6]


import statistics
exemple = [1,2,3,4,4,5,6] 
# la moyenne, ou plus précisément la moyenne arithmétique, est la somme de toutes les valeurs d'un ensemble de données divisée par le nombre de valeurs dans cet ensemble
statistics.mean(exemple)
print(statistics.mean(exemple))
#3.5714285714285716
# la médiane est la valeur qui sépare un ensemble de données en deux moitiés égales
statistics.median(exemple)
print(statistics.median(exemple))
# 4
# le mode est la valeur qui apparaît le plus fréquemment dans un ensemble de données
statistics.mode(exemple)
print(statistics.mode(exemple))
# 4
# la variance est une mesure de la dispersion des valeurs d'un ensemble de données par rapport à leur moyenne
statistics.variance(exemple)
print(statistics.variance(exemple))
#2.952
# l'écart type est la racine carrée de la variance, il mesure la dispersion des valeurs d'un ensemble de données
statistics.stdev(exemple)
print(statistics.stdev(exemple))
#1.718
#le quartile est une mesure statistique qui divise un ensemble de données en quatre parties égales
statistics.quantiles(exemple, n=4)
Q1 = statistics.quantiles(exemple, n=4)[0]
print(Q1)
# 2.5
Q2 = statistics.quantiles(exemple, n=4)[1]
print(Q2)
# 4
Q3 = statistics.quantiles(exemple, n=4)[2]
print(Q3)
# 5.5
# l'intervalle interquartile (IQR) est la différence entre le troisième quartile (Q3) et le premier quartile (Q1)
IQR = Q3 - Q1
print(IQR)
# 3.0
#boite à moustaches
import matplotlib.pyplot as plt

plt.boxplot(exemple)
plt.show()
# Analysons le taux d'intérêt et le montant du prêt
sns.scatterplot(HMDA_IL['interest_rate'],HMDA_IL['loan_amount'])
plt.show()



