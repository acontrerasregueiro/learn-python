"""Ahora vamos a leer otros datos futbolísticos, pero esta vez en remoto. 
Concretamente, vamos a acceder a información de la Premier League de la 
temporada 2010/2011. Esta información está de forma pública en un archivo JSON 
localizdo en 
https://raw.githubusercontent.com/openfootball/football.json/master/201011/en.1.clubs.json 
como se trata de un archivo remoto, accederemos mediante la librería PANDAS,
cuya cabecera debería empezar de la siguiente forma:"""

import pandas as pd

#leer un fichero en remoto con pandas
info = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2010-11/en.1.clubs.json")
#print(info)
for equipo in info['clubs']:
    print(equipo['name'])