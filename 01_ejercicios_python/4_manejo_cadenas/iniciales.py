"""
14. Escribe un archivo iniciales.py que solicite al usuario su nombre y apellidos y
devuelva sus iniciales en mayúsculas.
"""

nombre_completo = input("Dime tu nombre y apellidos: ")

palabras = nombre_completo.split()

iniciales = ""
for palabra in palabras:
    iniciales += palabra[0].upper()

print(f"Tus iniciales son: {iniciales}")