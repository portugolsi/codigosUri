a = int(input())

x = input().split(" ")
menor = 21
posicao = 0
for k in range(len(x)):
    if menor> int(x[k]):
        menor = int(x[k])
        posicao = k
print(posicao+1)
