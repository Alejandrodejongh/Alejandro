number= int(input("Ingrese un numero natural: "))
primos=[]
if number>0:
    for i in range(2, number):
        aux = number-1
        cont= 0
        while aux>1:
            if i%aux==0:
                cont +=1
                aux-=1
            else:
                aux-=1
                if cont==0:
                    primos.append(i)
                    break
                print(primos)
