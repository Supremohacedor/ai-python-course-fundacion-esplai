"""
17. Escribe un archivo fstrings_tabla.py que imprima una tabla con números del 1 al
10 y su respectivo cuadrado, alineando correctamente las columnas con f-
strings .
"""
print(f"{'Número':<8} {'Cuadrado':<8}")  # Esto alinea a la izquierda y reserva espacios (8).

for i in range(1, 11):
    print(f"{i:<8} {i**2:<8}")
