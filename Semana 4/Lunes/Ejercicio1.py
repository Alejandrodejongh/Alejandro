number= int(input("Ingrese un numero natural: "))
aux=1
oblongo=False
while aux<number:
    if aux*(aux+1)==number:
        oblongo=True
        break
    aux+=1
if oblongo:
    print("Es oblongo")
else:
    print("No es oblongo")