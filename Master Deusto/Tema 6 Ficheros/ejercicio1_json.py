import os
import json

data = {}
data['equipo'] = []
data['equipo'].append({
    'nombre':'Atletico de Madrid',
    'ciudad': 'Madrid',
    'puntos':'86'})
data['equipo'].append({
    'nombre':'Real Madrid',
    'ciudad': 'Madrid',
    'puntos':'84'})
data['equipo'].append({
    'nombre':'FC Barcelona',
    'ciudad': 'Barcelona',
    'puntos':'79'})

with open("liga.txt",'r+') as fp:
    json.dump(data,fp,indent=1)


with open("liga.txt","r+") as fp:
    
    data = json.load(fp)
    for equipo in data['equipo']:
        print(equipo['nombre'])
        print(equipo['ciudad'])
        print(equipo['puntos'])

