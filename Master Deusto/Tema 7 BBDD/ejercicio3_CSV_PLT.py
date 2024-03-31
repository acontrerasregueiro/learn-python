#Ejercicio importar CSV y generación de gráficas
import pandas as pandas
import matplotlib.pyplot as plt


csv = pandas.read_csv("http://users.stat.ufl.edu/~winner/data/world_wine.csv"
                      , sep=",")

#print(csv)
#Leemos la columna PerCap
columna_y = csv['PerCap']
numero_registros = 50

#Establecemos en Matplotlib que es un histograma con los valores y
plt.hist(columna_y,numero_registros)
print("Mostrando el grafico")
#Nombres para los ejes X e y, y el título del gráfico
plt.xlabel("Ingreso Medio")
plt.ylabel("Cantidad de registros")
plt.title('Histograma del ingreso medio')

plt.show()
