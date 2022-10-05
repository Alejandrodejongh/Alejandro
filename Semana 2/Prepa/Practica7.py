frase= str(input("Indique una frase: "))
letra= input("Indique una letra: ")
cont=0
for i in frase:
    if i== letra:
        cont+=1
print(f"La letra {letra} aparece {cont} veces en la frase: {frase}")
