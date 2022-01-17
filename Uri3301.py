h,z,l = [int(x) for x in input().split(" ")]
idades = [h,z,l]
idades.sort()
if idades[1]==z:
    print("zezinho")
elif idades[1]==h:
    print("huguinho")
else:
    print("luisinho")