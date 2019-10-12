# Pedir 3 números y mostrarlos de mayor a menor.

n1=float(input('Ingrese un número: '))
n2=float(input('Ingrese un segundo número: '))
n3=float(input('Ingrese un tercer número: '))
if n1>n2 and n1>n3 :
    if n2>n3 : 
        print(str(n1) +', '+str(n2)+', '+str(n3))
    else :
        print(str(n1) +', '+str(n3)+', '+str(n2))
elif n2>n1 and n2>n3 :
    if n1>n3 :
        print(str(n2) +', '+str(n1)+', '+str(n3))
    else :
        print(str(n2) +', '+str(n3)+', '+str(n1))
elif n3>n1 and n3>n2 :
    if n1>n2 :
        print(str(n3)+', '+str(n1)+', '+str(n2))
    else:
        print(str(n3) +', '+str(n2)+', '+str(n1))
