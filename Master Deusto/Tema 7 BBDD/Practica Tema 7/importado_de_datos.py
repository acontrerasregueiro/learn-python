#En este fichero a través de webscrapping descargamos y formateamos los datos
#Para posterior introducción en BBDD

from selenium import webdriver
from bs4 import BeautifulSoup
import time

canciones = []
def cargar_datos():
    wd = webdriver.Chrome()  #Utilizamos Edge al ser mas rápido.

    wd.get("""https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_
        uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_
        n%C3%BAmero_uno""")

    soup = BeautifulSoup(wd.page_source,'lxml')
    time.sleep(3)

    for elemento in soup.find_all('tr'):
        cancion_actual = []
        contador = 0
        if contador < 5:
            elemento.text.replace('\n','')
            elemento.text.replace('\xa0',' ')
            cancion_actual = elemento.text.split('\n',5)
            contador += 1
        else:
            contador = 0
        cancion_actual.pop(0)     #Eliminamos el primer elemento ya que estaba vacio  
        canciones.append(cancion_actual) 
        
    #Eliminamos del array los elementos no necesarios, no se corresponden a 
    #canciones, si no otra información de la página web
    canciones.pop(0)
    canciones.pop(0)
    canciones.pop(-1)
    canciones.pop(-1)
    canciones.pop(-1)
    canciones.pop(-1)
    canciones.pop(-1)

    for cancion in canciones:
        #Damos formato a la cadena para evitar duplicados al descargar datos de la web
        cancion[4] = cancion[4].replace('\n','')
        cancion[4] = cancion[4].replace('\xa0',' ').split(' ')
        
        #Formateamos las que tienen varios años, solo nos interesa el primer año
        cancion[2] = cancion[2][:4] 
        cadena = ''
        #Eliminamos elementos duplicados en pais descargados por webscrapping
        for palabra in cancion[4]:
            if len(cancion[4]) > 1:
                if palabra not in cadena:
                    cadena = cadena + palabra + ' '
        cancion[0]= cancion[0].rstrip()
        cancion[4] = cadena.rstrip()

#print(canciones)

 
def cargar_idioma_continente():
    #Introducimos los valores correspondientes al idioma y continente en la lista
    idioma = ['español', 'inglés', 'alemán', 'sueco', 'portugués', 'francés']
    continente = ['Europa', 'Asia', 'África', 'América del Norte', 'América del Sur', 'Oceanía'] 
     
    for cancion in canciones:
        match cancion[4]:
            case('Venezuela' | 'Puerto Rico' | 'Colombia' |'Argentina España' 
                | 'Colombia Trinidad y Tobago' | 'Cuba' | 'Venezuela'):
                cancion.append('America del sur')
                cancion.append('Español')    
            case('Estados Unidos' | 'Canadá'):
                cancion.append('America del norte')
                cancion.append('Inglés')
            case('España'):
                cancion.append('Europa')
                cancion.append('Español')
            case('Francia'):
                cancion.append('Europa')
                cancion.append('Francés')
            case('Reino Unido'):
                cancion.append('Europa')
                cancion.append('Inglés')
            case('Alemania'):
                cancion.append('Europa')
                cancion.append('Aleman')
            case('Suecia'):
                cancion.append('Europa')
                cancion.append('Sueco')
            case('Brasil'):
                cancion.append('America del sur')
                cancion.append('Portugues')
            case('Guyana'):
                cancion.append('America del sur')
                cancion.append('Inglés')
        

def eliminar_doble_pais():
    #Dado el enunciado solámente necesitamos el primer pais en la bbdd
    #Por lo que actualizamos la BBDD de los dos registros que vienene
    #Con doble país
    for cancion in canciones:
        if cancion[4] == 'Colombia Trinidad y Tobago':
            cancion[4] = 'Colombia'
        if cancion[4] == 'Argentina España':
            cancion[4] = 'Argentina'
        



        

