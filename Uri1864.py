letras = ['l','i','f','e'," ",'i','s',' ','n','o','t'," ",'a'," ",'p','r','o','b','l','e','m',' ','t','o',' ','b','e',' ','s','o','l','v','e','d']
a = int(input())

for k in range(a):
    if k==len(letras)-1:
        print(letras[k].upper())
    else:
        print(letras[k].upper(),end="")
