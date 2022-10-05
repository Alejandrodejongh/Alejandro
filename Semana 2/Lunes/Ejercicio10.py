option= int(input("Ingrese una opcion de pizza: \n1. Vegetariana  \n2. No vegetariana\n-> "))
if option== 1:
    ingrediente= input("Ingredientes vegetarianos, escoja uno: \n1. Pimiento \n2. Tofu\n->")
    if ingrediente== "Pimiento":
        print(f"Su pizza es vegetariana y tiene mozzarella, tomate y {ingrediente}")
    else: ingrediente== "Tofu"
    print(f"Su pizza es vegetariana y tiene mozzarella, tomate y {ingrediente}")
if option== 2:
    ingrediente= input("Ingredientes no vegetarianos, escoja uno: \n1. Peperoni \n2. Jamon\n3. Salmon\n->")
    if ingrediente== "Peperoni":
        print(f"Su pizza es no vegetariana y tiene mozzarella, tomate y {ingrediente}")
    elif ingrediente== "Jamon":
        print(f"Su pizza es no vegetariana y tiene mozzarella, tomate y {ingrediente}")
    elif ingrediente== "Salmon":
        print(f"Su pizza es no vegetariana y tiene mozzarella, tomate y {ingrediente}")