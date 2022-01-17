operador = input()
total = 0
coluna = 10
m = [[],[],[],[],[],[],[],[],[],[],[],[]]
for l in range(0,12):
    for c in range(0,12):
        m[l].append(float(input()))


if operador == "S":
    for l in range(1,6):
        for c in  range(11,coluna,-1):
            total += m[l][c]

        coluna -= 1

    coluna=7
    for l in range(6,11):
        for c in range(coluna,12):
            total+= m[l][c]
        coluna+=1

elif operador=="M":
    for l in range(1,6):
        for c in  range(11,coluna,-1):
            total += m[l][c]

        coluna -= 1

    coluna=7
    for l in range(6,11):
        for c in range(coluna,12):
            total+= m[l][c]
        coluna+=1
    total=total/30
print("%.1f"%total)