a = int(input())
decimal = []
result = 0
resto = 0
cont = 0
if a < 10:
    print("%d"%a)
elif a>=10 and a<=16:
    if a == 10:
        print("A")
    elif a == 11:
        print("B")
    elif a == 12:
        print("C")
    elif a == 13:
        print("D")
    elif a == 14:
        print("E")
    elif a == 15:
        print("F")
    elif a == 16:
        print("10")
else:
    while a >=16:
        decimal.append(a%16)
        a= a//16

    decimal.append(a)
    decimal.reverse()
    for k in range(len(decimal)):
        if k == len(decimal):
            if decimal[k] <= 9:
                print("%d"%decimal[k])
            elif decimal[k] == 10:
                print("A")
            elif decimal[k] == 11:
                print("B")
            elif decimal[k] == 12:
                print("C")
            elif decimal[k] == 13:
                print("D")
            elif decimal[k] == 14:
                print("E")
            elif decimal[k] == 15:
                if k == len(decimal):
                    print("F")
        elif decimal[k]<=9 :
            print(decimal[k],end="")
        elif decimal[k]==10:
            print("A",end="")
        elif decimal[k]==11 :
            print("B",end="")
        elif decimal[k]==12 :
            print("C",end="")
        elif decimal[k] == 13 :
            print("D",end="")
        elif decimal[k] == 14 :
            print("E",end="")
        elif decimal[k] == 15 :
            if k==len(decimal):
                print("F")
            else:
                print("F",end="")
print("\n")

"""if a < 10:
    print(a)
elif a>=10 and a<16:
    if a == 10:
        print("10")
    elif a == 11:
        print("11")
    elif a == 12:
        print("12")
    elif a == 13:
        print("13")
    elif a == 14:
        print("14")
    elif a == 15:
        print("15")
else:
    while a !=0:
        a = a//16
        b = a%16
        if a < 10:
            print(a)
        if a == 10:
            print("10")
        elif a == 11:
            print("11")
        elif a == 12:
            print("12")
        elif a == 13:
            print("13")
        elif a == 14:
            print("14")
        elif a == 15:
            print("15")"""
