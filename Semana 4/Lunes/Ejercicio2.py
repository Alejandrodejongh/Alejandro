
matriz1= {"sub1":[1,2,3],"sub2":[4,5,6]}
matriz2= {"sub3":[-1,0,1],"sub4":[0,1,1]}
for i,j in matriz1,matriz2:
    for h in "sub1":
        for o in "sub3":
            matfinal1=h[0]*o[0]+h[1]*o[1]+h[2]*o[2]
            print(matfinal1)