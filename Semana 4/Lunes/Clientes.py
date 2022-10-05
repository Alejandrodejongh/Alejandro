opcion=""
base_datos={}

while opcion !="6":
    opcion= input("Escoja una opcion: \n1-Agregar cliente\n2-Eliminar cliente\n3-Mostrar cliente\n4-Listar clientes\n5-Listar clientes preferentes\n6-Terminar\n-> ")

    if opcion=="1":
        nif= input("Indique NIF del cliente: ")
        nombre= input("Indique nombre del cliente: ")
        direccion= input("Indique direccion del cliente: ")
        telefono= input("Indique numero de telefono: ")
        correo= input("Indique correo electronico: ")
        preferente= input("Indique si es preferente: ")
        datos_personales={"Nombre":nombre,"Direccion":direccion,"Telefono":telefono,"Correo":correo,"Preferente":preferente}
        base_datos[nif]=datos_personales

    elif opcion=="2":
        nif= input("Indique NIF del cliente: ")
        base_datos.pop(nif)
        print("El cliente ha sido eliminado de la base de datos")

    elif opcion=="3":
            nif= input("Indique NIF del cliente: ")
            if nif in base_datos:
                for criterio,dato in base_datos[nif].items():
                    print(criterio,":", dato)
    elif opcion=="4":
        for nif,valor in base_datos.items():
            print(nif, valor["Nombre"])

    


        


