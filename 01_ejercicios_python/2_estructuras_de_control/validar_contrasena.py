"""
7. Escribe un archivo validar_contraseña.py que pida al usuario una contraseña y
verifique que cumpla los siguientes criterios:
Al menos 8 caracteres
Contiene mayúsculas y minúsculas
Contiene al menos un número
"""
user_password = input("Escribe tu contraseña: ")

# Escribo los criterios aparte
# c por carácter
min_caracteres = len(user_password) >= 8
tiene_mayus = any(c.isupper() for c in user_password)
tiene_minus = any(c.islower() for c in user_password)
tiene_num = any(c.isdigit() for c in user_password)

if not min_caracteres:
    print("La contraseña debe tener al menos 8 carácteres.")
elif not tiene_mayus:
    print("La contraseña debe contener mayúsculas.")
elif not tiene_minus:
    print("La contraseña debe contener minúsculas.")
elif not tiene_num:
    print("La contraseña debe contener un número.")
else:
    print("La contraseña cumple los criterios.")

