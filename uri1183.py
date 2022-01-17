operador = input().upper()
coluna = 1
total = 0
m = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
for l in range(0,12):
    for c in range(0,12):
        m[l][c] = float(input())
if operador == "S":
    for l in range(0, 12):
        for c in range(coluna, 12):
            total += m[l][c]
        coluna += 1
elif operador == "M":
    for l in range(0,12):
        for c in range(coluna,12):
            print(m[l][c],end=" ")
            total += m[l][c]
        print("\n")
        coluna+=1
    total = total/66
print("%.1f"%total)