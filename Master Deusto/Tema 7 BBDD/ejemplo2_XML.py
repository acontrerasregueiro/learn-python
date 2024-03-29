#Ejemplo XML

import xml.etree.cElementTree as ET
datos ='''
<concierto>
    <cartel>
        <grupo>
            <nombre>Nirvana</nombre>
            <miembros type="intl">3</miembros>
            <discos type="intl">10</discos>
        </grupo>
        <grupo>
            <nombre>Foo Fighters</nombre>
            <miembros type="intl">6</miembros>
            <discos type="intl">10</discos>
        </grupo>
        <grupo>
            <nombre>Pearl Jam</nombre>
            <miembros type="intl">6</miembros>
            <discos type="intl">11</discos>
        </grupo>
    </cartel>
</concierto> 
'''

concierto =ET.fromstring(datos)
lista = concierto.findall('cartel/grupo')
print("TOTAL DE GRUPOS :", len(lista))
for item in lista:
    print("******************************")
    print("Nombre", item.find('nombre').text)
    print("Miembros", item.find('miembros').text)
    print("Discos", item.find('discos').text)
