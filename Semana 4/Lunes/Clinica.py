pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}

opcion=""
while opcion != "3":
    opcion=input("Que desea hacer: \n1.Registrar Pacientes\n2.Ver Pacientes\n3.Salir\n->")
    if opcion== "1":
        
        nombre= input("Indique el nombre del paciente: ")
        apellido= input("Indique el apellido del paciente: ")
        cedula= int(input("Indique la cedula del paciente: "))
        id=int((input("Indique la id de su enfermedad: ")))
        for sistema, enfermedades in pathologies.items():
            for enfermedad in enfermedades:
                    for valores in enfermedad.items():
                        if enfermedad.get("id")==id:
                         datos_paciente={"Nombre: ":nombre, "Apellido: ":apellido, "Cedula: ":cedula, "id: ":id, "Enfermedad: ":enfermedad.get("name") }
                         for keys,values in datos_paciente.items():
                            print(keys,values)   

    
                
                
                
                #if system.get("id")==id:
                    #datos_paciente={"Nombre:": nombre, "Apellido:": apellido, "Cedula:": cedula, "Id": id}