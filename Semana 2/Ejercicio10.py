option= int(input("Ingrese una opción de pizza: 1- Vegetariana 2- No vegetariana"))
if option == "1":
    ingredientes= int(input("Ingrese una opción de ingredientes: 1- Pimiento 2- Tofu"))
    if ingredientes == "1":
        ingredientes = "Pimiento"
    else:
        ingredientes = "Tofu"
elif option == "2":
    ingredientes2= int(input("Ingrese una opción de ingredientes: 1- Peperoni 2- Jamón 3- Salmón"))
    if ingredientes2 == "1":
        ingredientes2 = "Peperoni"
    elif ingredientes2 == "2":
        ingredientes2 = "Jamón"
    else:
        ingredientes2 = "Salmón"
else:
    print("Invalid Option")