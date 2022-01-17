a = input().split(" ")
b = input().split(" ")
a1=int(a[0])
a2=int(a[1])
a3=int(a[2])

b1 = int(b[0])
b2 = int(b[1])
b3 = int(b[2])
b11 = 0
b22 = 0
b33 = 0
if b1>a1:
    b11 = b1-a1
if b2>a2:
    b22=b2-a2
if b3>a3:
    b33=b3-a3
print(b11+b22+b33)
