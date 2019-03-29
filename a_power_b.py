def a_power_b(a,b):
    cont=1

    for i in range(0,b):
        cont=(cont*a)
  

a=int(input("dijite el numero que quieres elevar"))
b=int(input("dijite el numero elevado"))
res=a_power_b(a,b)
print(res)
