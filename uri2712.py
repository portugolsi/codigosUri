a = int(input())
for k in range(a):
    validador = input()
    if validador[0:3].isupper():
        if validador[3]=="-":
            if validador[4:7].isdigit():
                if validador[7]=="1" or validador[7]=="2":
                    print("MONDAY")
                elif validador[7]=="3" or validador[7]=="4":
                    print("TUESDAY")
                elif validador[7] == "5" or validador[7] == "6":
                    print("WEDNESDAY")
                elif validador[7]=="7" or validador[7]=="8":
                    print("THURSDAY")
                elif validador[7]=="9" or validador[7]=="0":
                    print("FRIDAY")

            else:
                print("FAILURE")
        else:
            print("FAILURE")
    else:
        print("FAILURE")