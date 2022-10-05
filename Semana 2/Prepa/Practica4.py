punctuation= float(input("Indique su puntuacion: "))
money=2400
if punctuation==0:
    print(f"Su nivel es inaceptable, recibira {money}$")
elif punctuation==0.4:
    print(f"Su nivel es aceptable, recibira {money*punctuation + money}$")
elif punctuation>=0.6:
    print(f"Su nivel es meritorio, recibira {money*punctuation + money}$")