a = int(input())
for k in range(a):
    s = input().split(" ")
    n1 = s[0]
    p1 = s[1]
    n2 = s[2]
    p2 = s[3]
    n = input().split(" ")
    num1 = int(n[0])
    num2 = int(n[1])
    result = (num1+num2)%2
    if result==0:
        if p1=="PAR":
            print(n1)
        else:
            print(n2)
    else:
        if p1=="IMPAR":
            print(n1)
        else:
            print(n2)