#Con este modulo introducimos varios datos manualmente para verificar
#el correcto funcionamiento del software
import classes as clase

cancion = {"titulo" :"Hola","grupo" : "ACDC" ,"genero" : "ROCK"}
persona = {"dni" : "34898103L","nombre" :" Javier Lopez Lopez", "poblacion" : 
    "Madrid" ,"pais": "España"}

cancion_1 = {"titulo" :"Jaguar","grupo" : "Carl Cox" ,"genero" : "TECHNO"}
persona_1 = {"dni" : "01234567L","nombre" :"Emilio Gutierrez", "poblacion" : 
    "Galicia" ,"pais": "España"}

cancion_2 = {"titulo" :"Como los gorilas","grupo" : "Melody" ,"genero" : "POP"}
persona_2 = {"dni" : "12345678K","nombre" :"Gonzalo Lopez Miramontes", "poblacion" : 
    "Oporto" ,"pais": "Portugal"}

cancion_3 = {"titulo" :"La Cancion","grupo" : "Los Chunguitos" ,"genero" : "RUMBA"}
persona_3 = {"dni" : "87654321K","nombre" :"Ricardo Fon Ter", "poblacion" : 
    "Madrid" ,"pais": "España"}

def cargar():    
    favorita = clase.Favoritas(persona,cancion)
    
    favorita.mostrar_favorita()
    favorita_1 = clase.Favoritas(persona_1,cancion_1)
    favorita_1.mostrar_favorita()
    favorita_2 = clase.Favoritas(persona_2,cancion_2)
    favorita_2.mostrar_favorita()
    favorita_3 = clase.Favoritas(persona_3,cancion_3)
    favorita_3.mostrar_favorita()

