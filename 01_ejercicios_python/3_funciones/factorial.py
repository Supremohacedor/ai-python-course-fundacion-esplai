"""
11. Escribe un archivo factorial.py que defina una función que reciba un número
n y retorne su factorial usando recursión.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1 #Este valor se pone para que no haga mult con none
    else:
        return n * factorial(n - 1)

n = int(input("Dime un número: "))

resultado = factorial(n)
print(f"El factorial de {n} es {resultado}.")