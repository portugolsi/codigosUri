A = int(input())
cont=1
vencedor = 0
for k in range(A):
     #Se "1" Jog1, se "2" Jog2, Se 0 empate
    a = input().split(" ")
    j = a[0]
    i = a[1]
    if j == ("tesoura"):
        if i == "papel":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "pedra":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "Spock":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "lagarto":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "tesoura":
            vencedor = 0
            print("Caso #%d: De novo!" % cont)
            cont += 1
    elif j == ("pedra"):
        if i == "papel":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "pedra":
            vencedor = 0
            print("Caso #%d: De novo!" % cont)
            cont += 1
        elif i == "Spock":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "lagarto":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "tesoura":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
    elif j == ("papel"):
        if i == "papel":
            vencedor = 0
            print("Caso #%d: De novo!" % cont)
            cont += 1
        elif i == "pedra":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "Spock":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "lagarto":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "tesoura":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
    elif j == ("Spock"):
        if i == "papel":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "pedra":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "Spock":
            vencedor = 0
            print("Caso #%d: De novo!" % cont)
            cont += 1
        elif i == "lagarto":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "tesoura":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
    elif j == ("lagarto"):
        if i == "papel":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "pedra":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1
        elif i == "Spock":
            vencedor = 1
            print("Caso #%d: Bazinga!" % cont)
            cont += 1
        elif i == "lagarto":
            vencedor = 0
            print("Caso #%d: De novo!" % cont)
            cont += 1
        elif i == "tesoura":
            vencedor = 2
            print("Caso #%d: Raj trapaceou!" % cont)
            cont += 1