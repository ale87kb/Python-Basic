# Pedir un número entre el 0 y el 9999 y decir cuántas cifras tiene.
numero=input('Escriba un número entre 0 y 9999: ')
if int(numero)>=0 and int(numero)<=9999 :
    print('Cantidad de cifras: '+str(len(numero)))
else :
    print('Su número no cumple la condición')
