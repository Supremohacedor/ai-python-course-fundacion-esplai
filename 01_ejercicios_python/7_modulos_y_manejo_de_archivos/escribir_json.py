"""
24. Escribe un archivo escribir_json.py que guarde un diccionario en un archivo
JSON llamado datos.json . Luego, crea otro archivo leer_json.py que lo lea e
imprima su contenido.
"""
import json

datos = {
    "nombre": "Sara",
    "estudiante": True,
    "cursos": ["Python", "ASIR"]
}

with open("datos.json", "w") as archivo: #Lo abre y writes
    json.dump(datos, archivo, indent=4)

print("Diccionario guardado en datos.json")

