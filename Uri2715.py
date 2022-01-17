while True:
    try:
        a = int(input())
        numeros = [int(x)for x in input().split(" ")]
        contador = 0
        for k in range(a):
            contador+=numeros[k]

        contador1 = 0


        while contador-contador1 !=1 or contador-contador1!=0:
            contador1=numeros[k]
            k=k+1
        print(contador-contador1)
    except:
        break