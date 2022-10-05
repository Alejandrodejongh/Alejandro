jugador1= input("Indique nombre del primer jugador: ")
jugador2= input("Indique nombre del segundo jugador: ")
print("¡A jugar piedra, papel o tijeras!")
opt1= input(str(jugador1) + " escoja piedra, papel o tijeras: ".title())
opt2= input(str(jugador2) + " escoja piedra, papel o tijeras: ".title())
opt3= "Empate"
if opt1== "Piedra" and opt2== "Tijeras":
    print(f"{jugador1} gana usando Piedra")
elif opt1== "Piedra" and opt2== "Papel":
    print(f"{jugador2} gana usando Papel")
elif opt1== "Piedra" and opt2== "Piedra":
    print(opt3)
if opt1== "Papel" and opt2== "Tijeras":
    print(f"{jugador2} gana usando Tijeras")
elif opt1== "Papel" and opt2== "Piedra":
    print(f"{jugador1} gana usando Papel")
elif opt1== "Papel" and opt2== "Papel":
    print(opt3)
if opt1== "Tijeras" and opt2== "Piedra":
    print(f"{jugador2} gana usando Piedra")
elif opt1== "Tijeras" and opt2== "Papel":
    print(f"{jugador1} gana usando Tijeras")
elif opt1== "Tijeras" and opt2== "Tijeras":
    print(opt3)
