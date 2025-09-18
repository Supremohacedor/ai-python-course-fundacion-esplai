"""
25. Escribe un archivo clase_persona.py que defina una clase Persona con atributos
nombre y edad , y un método que imprima un saludo con su nombre.
"""

class Persona:
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad

    def saludar(self): #Método
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 35)
persona1.saludar()