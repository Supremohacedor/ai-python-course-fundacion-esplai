"""
27. Escribe un archivo validar_email.py que valide si un correo electrónico
ingresado por el usuario tiene un formato correcto usando expresiones
regulares
"""
import re #Este módulo trabaja con expresiones regulares

print("Este script verifica si tu email tiene un formato correcto.")
email = input("Escribe tu email: ")

# if "@" in email and "." in email and " " not in email:
#     print("El email tiene un formato correcto.")
# else:
#     print("El email no tiene un formato correcto.")

# Con expresiones regulares:
patron = '.+@.+\..+'

# Patrón:
# .+    : uno o más caracteres de cualquier tipo 
# @     : símbolo arroba obligatorio
# .+    : uno o más caracteres (dominio)
# \.    : un punto literal
# .+    : uno o más caracteres (extensión del dominio)


if re.match(patron, email):
    print("El email tiene un formato correcto.")
else:
    print("El email no tiene un formato correcto.")
