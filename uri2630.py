a = int(input())
cont = 1
for k in range(a):
    tipo = input()
    num = input().split(" ")
    n1 = int(num[0])
    maior = n1
    menor = n1
    n2 = int(num[1])
    if n2<menor:
        menor = n2
    if n2>=maior:
        maior = n2
    n3 = int(num[2])
    if n3>=maior:
        maior = n3
    if n3<menor:
        menor = n3
    if tipo == "min":
        print("Caso #%d: %d"%(cont,menor))
        cont+=1
    elif tipo == "max":
        print("Caso #%d: %d"%(cont,maior))
        cont += 1
    elif tipo == "mean":
        media = (n1+n2+n3)/3
        print("Caso #%d: %d"%(cont,media))
        cont += 1
    elif tipo == "eye":
        p = (0.3*n1)+(0.59*n2)+(0.11*n3)
        print("Caso #%d: %d"%(cont,p))
        cont += 1


