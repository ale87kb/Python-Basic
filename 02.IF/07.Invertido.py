# Pedir un número entre 0 y 9999 y mostrarlo invirtiendo sus cifras.
n=int(input('Escriba un número entre 0 y 9999: '))
if n>= 0 and n<=9999 :
    cifra=n
    invertido=''
    if(n>999):
        unidad=n//1000
        invertido=str(unidad)
        cifra=n-(unidad*1000)
    if(n>99):
        unidad=cifra//100
        invertido=str(unidad)+invertido
        cifra=cifra-(unidad*100)
    if(n>9):
        unidad=cifra//10
        invertido=str(unidad)+invertido
        cifra=cifra-(unidad*10)
    
    unidad=cifra//1
    invertido=str(unidad)+invertido
    
    print(invertido)
    
else :
    print('Su número no cumple la condición.')

        
