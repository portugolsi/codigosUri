x = input().split(' ')
a = int(x[0])
b = int(x[1])
c = int(x[2])
if (a>b):
    if (a>c):
        print("%d eh o maior"% a)
    else:
        print("%d eh o maior"% c)
elif (b>c):
    print("%d eh o maior" % b)
else:
    print("%d eh o maior" % c)


