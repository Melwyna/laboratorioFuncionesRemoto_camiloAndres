def elevado():
    cont=1
    a=int(input("dijite el numero que quieres elevar"))
    b=int(input("dijite el numero elevado"))
    for i in range(0,b):
        cont=(cont*a)
    print(cont)

elevado()
