personaldict={}
while True:
    dato= input("Que tipo de dato quiere almacenar: ")
    valordato= input("Ingrese dicho dato: ")
    personaldict[dato]=valordato

    for key,value in personaldict.items():
        print(f"Su {key} es {value}")
    
    if input("Desea salir:\nYes->\nNo->\n ")=="Y":
        break
