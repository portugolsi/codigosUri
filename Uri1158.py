a = int(input())

for k in range (a):
    contador = 0
    total = 0
    j = input().split(" ")
    a1 = int(j[0])
    a2 = int(j[1])
    while contador != a2:
        if a1%2==1:
            total += a1
            a1 +=2
            contador +=1

        else:
            total += a1+1
            a1 +=2
            contador += 1


    print(total)
