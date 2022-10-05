lista= "Bienvenidos a la prepa de algoritmos"
count = 0
for i in lista:
    if i== "a" and len(lista)>count+1:
        if lista[count+1]=="l":
            print(f"Hay una al en el punto {count} y {count+1}")
    count +=1