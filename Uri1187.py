m = [[],[],[],[],[],[],[],[],[],[],[],[]]
operador = input()
CI = 1
CF = 11
LI = 0
total = 0
for l in range(0,12):
    for c in range(0,12):
        m[l].append(float(input()))
if operador == "S":
    for l in range(0,5):
        for c in range(CI,CF):
            total += m[l][c]
        CI +=  1
        CF -=1
elif operador == "M":
    for l in range(0,5):
        for c in range(CI,CF):
            total += m[l][c]
        CI +=  1
        CF -=1
    total = total/30
print("%.1f"%total)