cesta={}
while True:
    continuar="Y"
    if input("Desea anadir un articulo a la lista \nYes->\nNo->\n->")==continuar:
        articulo= input("Ingrese el articulo de compra: ")
        precio= float(input("Ingrese el precio de dicho articulo: "))
        cesta[articulo]=precio
    elif continuar==False:
        for articulos,precios in cesta.items():
            print(articulos, precios)
    break
    
