a = int(input())
while a !=0:

    divisax,divisay = [int(x) for x in input().split(" ")]
    for k in range(0,a):
        x,y = [int(x) for x in input().split(" ")]
        if x==divisax or y == divisay:
            print("divisa")
        else:
            if x>divisax:
                if y>divisay:
                    print("NE")
                else:
                    print("SE")
            else:
                if y>divisay:
                    print("NO")
                else:
                    print("SO")
    a = int(input())