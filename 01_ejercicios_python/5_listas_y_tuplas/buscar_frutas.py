"""
19. Escribe un archivo buscar_frutas.py que cree una tupla con nombres de frutas
y permita al usuario ingresar un nombre para verificar si está en la tupla.
"""

tupla = ("manzana", "naranja", "uva")

fruta_buscada = input("Dime una fruta para verificar si está en la tupla: ")

if fruta_buscada in tupla:
    print(f"La fruta {fruta_buscada} se encuentra en la tupla.")
else:
    print(f"La fruta {fruta_buscada} no se encuentra en la tupla.")
