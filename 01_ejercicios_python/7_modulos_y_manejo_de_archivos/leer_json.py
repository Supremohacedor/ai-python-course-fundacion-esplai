import json

with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)  # Carga el contenido JSON en un diccionario

print("Contenido de datos.json:")
print(datos_cargados)
