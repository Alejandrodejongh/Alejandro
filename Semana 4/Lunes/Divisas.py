divisa=input("Ingrese una divisa: ")
dict_divisa={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print(dict_divisa.get(divisa.title(), "La moneda no fue encontrada"))