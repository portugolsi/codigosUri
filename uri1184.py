m = [[],[],[],[],[],[],[],[],[],[],[],[]]
operador = input()
coluna = 1
total = 0
for l in range(0,12):
    for c in range(0,12):
        a = float(input())
        m[l].append(a)
if operador.upper() == "S":
    for l in range(1,12):
        for c in range(0,coluna):
            total += m[l][c]
        coluna+=1
elif operador.upper() == "M":
    for l in range(1,12):
        for c in range(0,coluna):
            total+= m[l][c]
        coluna+=1
total = total/66

print("%.1f"%total)
