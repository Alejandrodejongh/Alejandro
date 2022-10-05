edad= int(input("Indique su edad: "))
if edad<4:
    print("Su entrada es gratis")
elif edad>=4 and edad<=18:
    print("Debe pagar 5$")
else:
    print("Debe pagar 10$")
