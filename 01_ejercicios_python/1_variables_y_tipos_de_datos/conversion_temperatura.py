"""
3. Escribe un archivo conversion_temperatura.py que convierta grados Celsius a
Fahrenheit y viceversa.
"""

tipo = input("¿En qué formato vas a dar la temperatura? F | C : ")
temp = int(input('Introduce una temperatura: '))


if tipo == "F":
    temp = (temp - 32) * 5 / 9
    print(f"La temperatura es {temp}")
elif tipo == "C":
    temp = (temp * 9 / 5) + 32
    print(f"La temperatura es {temp}")
