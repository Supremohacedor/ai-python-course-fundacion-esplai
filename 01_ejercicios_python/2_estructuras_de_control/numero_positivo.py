"""
4. Escribe un archivo numero_positivo.py que solicite al usuario un número e
indique si es positivo, negativo o cero.
"""
print("Te voy a indicar si un número es positivo, negativo o cero.")
num = int(input("Dime un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es 0.")