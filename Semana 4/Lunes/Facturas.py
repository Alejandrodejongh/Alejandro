facturas={}
cobrado=0
falta=0
opcion=""
while opcion !="Terminar":
    opcion=input("Que desea hacer: \nAgregar Factura\nPagar Factura\nTerminar\n-> ")
    if opcion.title()=="Agregar Factura":
        numerofactura= (input("Indique el numero de la factura: "))
        costefactura= float(input("Indique el coste de dicha factura: "))
        facturas[numerofactura]=costefactura
        falta+=costefactura
    elif opcion.title()== "Pagar Factura":
        numerofactura= int(input("Indique el numero de la factura: "))
        for num,costes in facturas.items():
            if num==numerofactura:
                facturas.pop(numerofactura)
                falta-=costefactura
    print(cobrado)
    print(falta)
