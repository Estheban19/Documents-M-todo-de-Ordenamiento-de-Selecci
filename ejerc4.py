palabras=input("ingresa una lista de palabras separado por coma:")
lista_palabras=palabras.split(',')
palabra_mas_larga=""

for palabra in lista_palabras:
    if len(palabra_mas_larga)>(palabra):
        palabra=palabra_mas_larga=palabra
print("la palbra mas larga es :", palabra_mas_larga)