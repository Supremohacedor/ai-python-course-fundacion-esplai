"""
26. Escribe un archivo clase_coche.py que defina una clase Coche con atributos
marca y modelo , y un método que imprima su descripción
"""
class Coche:
    def __init__(self, marca, modelo): 
        self.marca = marca
        self.modelo = modelo

    def describir(self): #Método
        print(f"El coche es de la marca {self.marca} y es el modelo {self.modelo}.")

coche1 = Coche("Seat", "Panda")
coche1.describir()