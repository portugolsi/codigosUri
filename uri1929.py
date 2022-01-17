numeros= input()
novos = ["1","2","3","4"]
contador = 0
digitos = 1
numero = ""
for k in range(len(numeros)):
    if numeros[k].isdigit():
        if (k+1)==len(numeros):
         numero+=numeros[k]
         novos[contador] = numero
        else:
            numero += numeros[k]

    else:
        novos[contador] = numero
        contador += 1
        numero = ""


a = int(novos[0])
b = int(novos[1])
c = int(novos[2])
d = int(novos[3])
numero = [a,b,c,d]
numero.sort()
a = numero[0]
b = numero[1]
c = numero[2]
d = numero[3]

if (a+b>c) and (a+c>b) and (c + b > a):
    print("S")
elif (b+c>d) and (b+d>c) and (c + d > b):
    print("S")
else:
    print("N")