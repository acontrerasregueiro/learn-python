# 4.13 Page 67
comida = ('espaguettis','arroz','pollo', 'churrasco', 'ensalada')
print(comida)
# comida[1] = True Son inmutables no se puede modificar solo un elemento pero si toda la tupla
comida = ('espaguettis','arroz','pollo', 'churrasco', 'ensalada','pavo', 'queso')
print(comida)

for plato in comida:
    print(plato)