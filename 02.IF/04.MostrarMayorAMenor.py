# Pedir 2 números y mostrarlos de mayor a menor.

n1=float(input('Ingrese un número: '))
n2=float(input('Ingrese un segundo número: '))
if n1>n2 :
    print(str(n1) +', '+str(n2))
else :
    if n1==n2 :
        print(str(n1) +', '+str(n2))
    else :
        print(str(n2) +', '+str(n1))
