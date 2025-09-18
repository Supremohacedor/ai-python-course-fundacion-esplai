"""
9. Escribe un archivo numero_primo.py que contenga una función es_primo(n) para
determinar si un número es primo.
"""
def esprimo(n):
    if n <= 1:
        print(f"El número {n} no es primo.")
        return
    
    for i in range(2, n):
        if n % i == 0:
            print(f"El número {n} no es primo.")
            return
        
    print(f"El número {n} es primo.")

n = int(input("Dime un número: "))

esprimo(n)