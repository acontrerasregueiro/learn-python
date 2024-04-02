#Módulo para generar gráfica de todas las canciones en el número 1
import pandas as pandas
import matplotlib.pyplot as plt

def generar_grafico_porcentaje():
    fig,ax = plt.subplots()
    Data = pandas.read_html("https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno",header=0)

    canciones = (Data[1]['Tema']) 
    semanas = ((Data[1]['Semanas']*100)/52)

    ax.bar(canciones,semanas)

    ax.set_ylabel("Porcentaje")
    ax.set_title("Porcentaje semanas número 1")


    plt.show()
#generar_grafico_porcentaje()