frase= input("Indique una frase: ")
cont=0
for vocal in frase:
        if vocal=="a":
            print(f"Hay {cont} a en la frase")
        elif vocal== "e":
            print(f"Hay {cont} e en la frase")
        elif vocal== "i":
            print(f"Hay {cont} i en la frase")
        elif vocal== "o":
            print(f"Hay {cont} o en la frase")
        elif vocal== "u":
            print(f"Hay {cont} u en la frase")
        cont+=1