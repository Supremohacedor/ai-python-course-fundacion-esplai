"""
10. Escribe un archivo filtrar_pares.py que contenga una función filtrar_pares(lista) , la
cual recibe una lista de números y devuelve otra lista con solo los números
pares.
"""
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nueva = []

def filtrar_pares(lista):
    for num in lista:
        if num % 2 == 0:
            lista_nueva.append(num)
    print(lista_nueva)

filtrar_pares(lista)
