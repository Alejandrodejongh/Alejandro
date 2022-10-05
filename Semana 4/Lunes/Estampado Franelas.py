info = {
    "shirt_sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    "colors": {
        "plain": "white,black,blue,gray",
        "tie-dye": "rainbow,acid wash"
    },
    "print_sizes": [[(10, 10), 12.30], [(20, 15), 14.60]]
}

option= ""
while option !="4":
    option= input("Que desea hacer: \n1.Registrar Compra\n2.Ver Compras\n3.Catalogo\n4.Salir\n->")
    if option=="1":
        datos_compra={}
        cedula= (int(input("Indique su numero de cedula: ")))
        talla= input("Que talla desea: ")
        color= input("De que color la desea: ")
        estampado= input("Tamano de estampado: ")
        datos_compra={"Cedula:":cedula, "Talla:":talla, "Color:":color, "Estampado:":estampado}
    #elif option=="2":
    elif option== "3":
        for keys, values in info.items():
            tallas= info.get("shirt_sizes")
            colores= info.get("colors")
            estampado= info.get("print_sizes")
            print("Tallas:", tallas)
            print("Colores:", colores)
            print("Estampado:", estampado)
