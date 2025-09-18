"""
13. Escribe un archivo contar_vocales.py que cuente cuántas veces aparece cada
vocal en una cadena ingresada por el usuario.
"""
frase = input("Dime una frase: ")

vocales = "aeiou"

for vocal in vocales:
    num = frase.count(vocal)
    print(f"La vocal {vocal} aparece {num} veces.")