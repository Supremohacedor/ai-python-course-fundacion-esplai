"""
21. Escribe un archivo frecuencia_palabras.py que cuente la frecuencia de palabras
en un texto ingresado por el usuario.
"""

texto_usuario = input("Escribe un texto: ")

palabras = texto_usuario.split()

frecuencia = {}

#Los diccionarios permiten trabajar con textos grandes!
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

for palabra, cantidad in frecuencia.items():
    print(f"La palabra {palabra} aparece {cantidad} veces.")
