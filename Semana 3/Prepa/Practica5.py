lista=[]
contrasena= (input("Indique una contraseña: "))
while True:
    if len(contrasena)<8:
        print("La contrasena debe ser mayor a 8 caracteres")
        break
    elif len(contrasena)>8:
        for x in contrasena:
            if x.lower()==False:
               continue
            if x.upper()==False:
                continue
    else:
        print("La contrasena debe tener una mayuscula y una minuscula")

    
    
