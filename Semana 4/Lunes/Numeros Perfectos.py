number=int(input("Ingrese un numero entero: "))
divisores_propios=[]
while True:
    for i in range(1,number):
        if number%i==0:
            divisores_propios.append(i)
    if sum(divisores_propios)==number:
        print(f"El numero {number} es perfecto")
    else:
        print(f"El numero {number} no es perfecto")
        break
