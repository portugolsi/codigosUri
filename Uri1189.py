m = [[],[],[],[],[],[],[],[],[],[],[],[]]
operador = input()
CF = 1
total=0
for l in range(0,12):
    for c in range(0,12):
        m[l].append(float(input()))
if operador == "S":
    for l in range(1,6):
        for c in range(0,CF):
            total += m[l][c]
        CF+=1
    CF = 5
    for l in range(6,12):

        for c in range(0,CF):
            total += m[l][c]
        CF-=1
elif operador == "M":
    for l in range(1, 6):
        for c in range(0, CF):
            total += m[l][c]
        CF += 1
    CF = 5
    for l in range(6, 12):

        for c in range(0, CF):
            total += m[l][c]
        CF -= 1
    total = total/30
print("%.1f"%total)