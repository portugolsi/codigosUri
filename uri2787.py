n1 = int(input())
n2 = int(input())
if n1%2==0:
    if n2%2==0:
        print(1)
    else:
        print(0)
else:
    if n2%2==0:
        print(0)

    else:
        print(1)