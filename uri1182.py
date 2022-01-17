coluna= int(input())
operador = input()
total = 0
m = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
for l in range(0,12):
    for c in range(0,12):
        m[l][c] = float(input())
if operador == "S":
    for l in range(0,12):
        for c in range(0,12):
            if c == coluna:
                total += m[l][coluna]
elif operador == "M":
    for l in range(0, 12):
        for c in range(0,12):
            if c == coluna:
                total += m[l][coluna]
    total = total/12
print("%.1f"%total)