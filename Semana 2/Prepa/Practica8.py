numero= int(input("Indique un numero entero: "))
for i in range(2,numero-1):
    if numero%i==0:
        print(f"El numero {numero} no es primo")
        break
    else:
        print(f"El numero {numero} es primo")
        break
if numero== 1:
    print("El numero 1 no es primo")