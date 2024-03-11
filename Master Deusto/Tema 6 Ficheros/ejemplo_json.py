import json
data = {} 
data['usuario'] =[] 
data['usuario'].append({'nombre':'Josep',
                        'apellidos':'Estarlich',
                        'edad':29})
data['usuario'].append({'nombre':'Claudio',
                        'apellidos':'Garcia',
                        'edad':35})
data['usuario'].append({'nombre':'Claudio',
                        'apellidos':'Gomez',
                        'edad':33})
#escribimos el contenido en el fichero 
with open('./prueba.txt', 'r+') as  fichero:
    json.dump(data,
              fichero,
              indent=1)
    #Mostramos el contenido 
    contenido= json.dumps(data)
    print(contenido) 
    print("---------") #Adecuamos los datos en pantalla 
    with open('./prueba.txt') as fichero:
        data=json.load(fichero)
        for usuario in data['usuario']:
            print(usuario['nombre'])
            print(usuario['apellidos'])    
            print(usuario['edad'])