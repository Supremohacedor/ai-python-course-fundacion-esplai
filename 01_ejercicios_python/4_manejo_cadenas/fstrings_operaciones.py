"""
16. Escribe un archivo fstrings_operaciones.py que reciba un número ingresado por
el usuario e imprima su cuadrado y su raíz cuadrada con formato de dos
decimales usando f-strings .
"""
print("Este script recibe un número e imprime su cuadrado y raíz cuadrada.")
num = int(input("Dime un número: "))

cuadrado = round(float(num ** 2), 2)
raiz = round(float(num ** 0.5), 2)

print(f"El cuadrado de {num} es {cuadrado} y la raiz de {num} es {raiz}.")
