num_terminos = int(input("Ingrese la cantidad de términos: "))

t1, t2 = 0, 1
print("Secuencia de Fibonacci:")

if num_terminos <= 0:
    print("No se puede mostrar la secuencia de Fibonacci para 0 términos.")
elif num_terminos == 1:
    print("Fibonacci", t1)
else:
    for i in range(num_terminos):
        print(t1)
        t1, t2 = t2, t1 + t2

      

            