import os
existe = os.access("/prueba.txt", os.F_OK)
print(existe) 
permiso = os.access("/prueba.txt", os.R_OK) 
print(permiso) 
permiso = os.access("/prueba.txt", os.W_OK)
print(permiso)
permiso = os.access("/prueba.txt", os.X_OK)
print(permiso)