"""
6. Escribe un archivo fibonacci.py que solicite un número al usuario y genere la
secuencia de Fibonacci hasta ese número.
"""
print("Voy a generar la secuencia de Fibonacci hasta el número que me digas.")
user_num = int(input("Dime un número: "))

# Guardamos los dos primeros números de Fibonacci
num1 = 0
num2 = 1

while num1 <= user_num:
    print(num1)
    # Cálculo de Fibonacci
    siguiente = num1 + num2
    anterior = num2
    # Actualizo el valor
    num1 = anterior
    num2 = siguiente
