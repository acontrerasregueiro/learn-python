import os
import json

data = {}
data['equipo'] = []
data['equipo'].append({
    'nombre':'Atletico de Madrid',
    'ciudad': 'Madrid',
    'puntos': 86,
    'posicion': 1})

data['equipo'].append({
    'nombre':'Real Madrid',
    'ciudad': 'Madrid',
    'puntos': 84,
    'posicion': 2})

data['equipo'].append({
    'nombre':'FC Barcelona',
    'ciudad': 'Barcelona',
    'puntos': 79,
    'posicion':3})
data['equipo'].append({
    'nombre':'Sevilla',
    'ciudad': 'Sevilla',
    'puntos':77,
    'posicion':4})
data['equipo'].append({
    'nombre':'Real Sociedad',
    'ciudad': 'San Sebastian',
    'puntos':62,
    'posicion': 5})
data['equipo'].append({
    'nombre':'Betis',
    'ciudad': 'Sevilla',
    'puntos':61,
    'posicion': 6})



with open("liga.txt","r+",encoding="utf-8",) as fp:
    json.dump(data,fp,indent=5)


with open("liga.txt","r+",) as fp:
    data = json.load(fp)
    print("*** Clasificación ***")
    for equipo in data['equipo']:
        if equipo['posicion']<= 4:
            print("El ",equipo['nombre'] ,"de la ciudad ",equipo['ciudad'], " finalizó la liga en ",equipo['posicion'], "posicion por lo que el próximo año jugará la Champions league")
        else:
            print("El ",equipo['nombre'] ,"de la ciudad ",equipo['ciudad'], " finalizó la liga en ", equipo['posicion'], "posicion por lo que el próximo año jugará la Europa league")
     

        


