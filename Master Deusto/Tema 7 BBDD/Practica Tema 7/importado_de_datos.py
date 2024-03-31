from selenium import webdriver
from bs4 import BeautifulSoup
import time

wd = webdriver.Edge()

wd.get("https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno")

soup = BeautifulSoup(wd.page_source,'lxml')
time.sleep(3)

canciones = []
#for elemento in soup.find_all('td'):
for elemento in soup.find_all('tr'):
    cancion_actual = []
    contador = 0
    if contador < 5:
        elemento.text.replace('\n','')
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
    cancion[4] = cancion[4]:-2
    print(cancion)
    #print(cancion[4].split(' '))
    #print(cancion[4].replace('\n',''))
    

    


        

