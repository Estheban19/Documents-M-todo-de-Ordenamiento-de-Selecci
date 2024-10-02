import re 

def verificar_contraseña(contraseña):
    if (len(contraseña) <8 or
        not re.search(r"[A-Z]",contraseña ) or
        not re.search(r"[a-z]",contraseña ) or
        not re.search(r"\d",contraseña ) or
        not re.search(r"[!$%&.]",contraseña )):
        return "contraseña invalida" 
    return "contraseña valida" 


valor=input("COLOQUE CONTRASEÑA: ")

valor2=verificar_contraseña(valor)
print(valor2)

if valor2 == "contraseña valida":
    with open("archiv.txt" ,"a") as archivo:
        archivo.write(valor+"n/")
    print("CORRECTO")
