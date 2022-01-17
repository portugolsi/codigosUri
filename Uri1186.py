m = [[],[],[],[],[],[],[],[],[],[],[],[]]
coluna = 11
total = 0
operador = input()
for l in range(0,12):
    for c in range(0,12):
        j = float(input())
        m[l].append(j)

if operador == "S":
    for l in range(1,12):
        for c in range(coluna,12):
            total += m[l][c]
        coluna-=1

elif operador == "M":
    for l in range(1,12):
        for c in range(coluna,12):
            if coluna==0:
                pass
            else:
                total += m[l][c]
        coluna-=1
    total = total/66
print("%.1f"%total)