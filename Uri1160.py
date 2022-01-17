casos = int(input())

for k in range(casos):
    contador = 0
    numeros = input().split(" ")
    pa = int(numeros[0])
    pb = int(numeros[1])
    taxaA = float(numeros[2])
    taxaB = float(numeros[3])
    while pa<=pb:
        pa = (pa + (pa*taxaA/100))//1
        pb = (pb + (pb*taxaB/100))//1
        contador +=1
    if contador<=100:
        print("%d anos." %contador)
    else:
        print("Mais de 1 seculo.")




