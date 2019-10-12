# Pedir 2 números y decir cual es mayor.

n1=float(input('Ingrese un número: '))
n2=float(input('Ingrese un segundo número: '))
if n1>n2 :
    print(str(n1) +' es mayor a '+str(n2))
else :
    if n1==n2 :
        print(str(n1) +' es igual a '+str(n2))
    else :
        print(str(n2) +' es mayor a '+str(n1))
