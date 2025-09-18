"""
20. Escribe un archivo capitales.py que cree un diccionario con países como
clave y sus capitales como valor. Luego, permite al usuario ingresar un país
y muestra su capital.
"""

capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Portugal": "Lisboa",
    "Japón": "Tokio" #La última no lleva coma
}

pais = input("Escribe el nombre de un país: ")

capital = capitales.get(pais)

print(f"La capital de {pais} es {capital}.")