linha = int(input())
operador = input()
total = 0
m = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
for l in range(0,12):
    for c in range(0,12):
        m[l][c] = float(input())
for l in range(0,12):
    for c in range(0,12):
        print(m[l][c]," | ", end="")
    print("\n")
if operador == "S":
    for c in range(0,12):
        total += m[linha][c]
elif operador == "M":
    for c in range(0, 12):
        total += m[linha][c]
    total = total/12
print("%.1f"%total)