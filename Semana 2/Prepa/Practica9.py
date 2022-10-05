contraseña= input("Indique su contraseña: ")
put= input("Coloque su contraseña: ")
while put:
    if put is not contraseña:
        put= input("Acceso denegado, intente de nuevo: ")
    if put is contraseña:
        print("Acceso concedido")
        break