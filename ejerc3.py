import re

def es_valida(contra):
    # Verifica si la contraseña tiene al menos una mayúscula, un número, un caracter especial, y es más larga que 6 caracteres
    if len(contra) < 6:
        return False
    if not re.search(r'[A-Z]', contra):
        return False
    if not re.search(r'\d', contra):
        return False
    if not re.search(r'[^a-zA-Z0-9]', contra):
        return False
    return True

contra = input("Ingrese la contraseña: ")

while not es_valida(contra):
    print("La contraseña es débil. Debe tener al menos una mayúscula, un número, un caracter especial, y ser más larga que 6 caracteres.")
    contra = input("Ingrese nuevamente la contraseña: ")

print("Contraseña válida.")