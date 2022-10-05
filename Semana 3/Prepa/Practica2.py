palabra= input("Indique una palabra: ")
alreves=palabra
palabra=list(palabra)
alreves=list(alreves)
alreves.reverse()
if palabra==alreves:
    print("La palabra es un palindromo")
else:
    print("No es un palindromo")