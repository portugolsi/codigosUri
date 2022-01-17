m = [[],[],[],[],[],[],[],[],[],[],[],[]]
operador = input()
coluna = 11
total = 0
for l in range(0,12):
    for c in range(0,12):
        j = float(input())
        m[l].append(j)
if operador=="S":

    for l in range(0,11):
        for c in range(0,coluna):
            total += m[l][c]
        coluna -=1
elif operador == "M":
    for l in range(0, 11):
        for c in range(0, coluna):
            total = total + m[l][c]
        coluna -=1

    total = total/66
print("%.1f"%total)