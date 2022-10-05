dict_fruta={"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
fruta= input("Ingrese una fruta: ")
kilos= float(input("Ingrese numero de kilos: "))
for f,p in dict_fruta.items():
    if f==fruta.title():
        preciototal=p*kilos
        print(f"El precio a pagar es {preciototal}$")
