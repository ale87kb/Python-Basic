# Pedir un número entre 0 y 9999 y mostrarlo invirtiendo sus cifras.
n=int(input('Escriba un número entre 0 y 9999: '))
if n>= 0 and n<=9999 :
    mil=n//1000
    cifra=n-1000*mil
    centena=cifra//100
    cifra = cifra-100*centena
    decena=cifra//10
    unidad = cifra-10*decena
    print(unidad, decena, centena, mil)
else :
    print('Su número no cumple la condición.')
