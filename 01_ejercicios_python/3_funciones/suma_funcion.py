"""
8. Escribe un archivo suma_funcion.py que defina una función sumar(a, b) que
reciba dos números y retorne su suma.
"""
def sumar(a,b):
    sum = a + b
    print(f"La suma de {a} y {b} es {sum}.")

num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

sumar(num1, num2)