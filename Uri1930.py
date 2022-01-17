a1, a2, a3, a4 =[int(x) for x in input().split(" ")]
numeros = [a1, a2, a3, a4]
numeros.sort()
numeros.reverse()
total = numeros[0]
cont = 1
for k in range(1,len(numeros)):
    total += numeros[cont]-1
    cont+=1
print(total)