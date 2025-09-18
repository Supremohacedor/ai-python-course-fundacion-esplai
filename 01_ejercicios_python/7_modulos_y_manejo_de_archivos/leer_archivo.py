"""
23. Escribe un archivo leer_archivo.py que lea un archivo llamado datos.txt y cuente
cuántas líneas tiene.
"""
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

print(f"El archivo tiene {len(lineas)} líneas.")