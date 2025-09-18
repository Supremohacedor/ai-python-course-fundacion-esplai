"""
2. Escribe un archivo operaciones_basicas.py que declare dos variables numéricas
y realice las operaciones básicas (+, -, *, /, %, //, **). Imprime los resultados
usando f-strings .
"""
num1 = 2
num2 = 3

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
modulo = num1 % num2
div_ent = num1 // num2
expon = num1 ** num2

print(f"La suma de {num1} y {num2} es {suma}.")
print(f"La resta de {num1} y {num2} es {resta}.")
print(f"La mult de {num1} y {num2} es {mult}.")
print(f"La div de {num1} y {num2} es {div}.")
print(f"El modulo de {num1} y {num2} es {modulo}.")
print(f"La división entera de {num1} y {num2} es {div_ent}.")
print(f"{num1} elevado a {num2} es {expon}.")
