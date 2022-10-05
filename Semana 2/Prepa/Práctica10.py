lista= "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
cont=0
for i in lista:
    if i== "o":
        if lista[cont+1]== "m":
            print(f"Hay at en {cont}-{cont+1}")
    cont+=1