"""
12. Escribe un archivo invertir_palabras.py que pida al usuario una frase y devuelva
la misma frase con cada palabra en orden inverso
"""
print("Escribe una frase y cada palabra estará en el orden inverso.")
frase = input("Dime una frase: ")

palabras = frase.split()

palabras_invertidas = []
for palabra in palabras:
    invertida = palabra[::-1] #Esto se llama slicing
    palabras_invertidas.append(invertida)

resultado = " ".join(palabras_invertidas)

print(resultado)
