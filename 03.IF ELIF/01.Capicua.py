# Pedir un número entre 0 y 9999 y decir si es capicúa.

n=int(input('Escriba un número entre 0 y 9999: '))
if n>=0 and n<=9999 :    
    mil=n//1000
    cifra=n-1000*mil
    centena=cifra//100
    cifra=cifra-100*centena
    decena=cifra//10
    unidad= cifra-10*decena
    if mil==unidad and centena==decena :
        print('Número capicúa')
    elif centena==unidad :
        print('Número capicúa')
    elif decena==unidad :
        print('Número capicúa')
    else :
        print('Número NO capicúa')
else :
    print('Su número no cumple la condición.')

    
