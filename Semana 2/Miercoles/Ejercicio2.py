number= int(input("Introduzca un numero: "))
aux = number-1
acum= 0
while aux >= 1:
    if number%aux == 0:
        acum+= aux

        