a = int(input())
for k in range(a):
    j = input().split(" ")
    n1 = j[0]
    n2 = j[1]
    tamanho = len(n1)-len(n2)
    if n1[tamanho:]==n2:
        print("encaixa")
    else:
        print("nao encaixa")