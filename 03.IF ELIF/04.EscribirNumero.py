# Pedir un número entre 0 y 99 y mostrarlo escrito en palabra. Ejemplo para mostrar 56 sería 'cincuenta y seis'. Usar print('Hola', end=' ').

n=int(input('Escriba un número entre 0 y 99: '))
if n>= 0 and n<=99 :
    if n>=0 and n<=15 :
        if n==0 :
            print('Cero')
        elif n==1 :
            print('Uno')
        elif n==2 :
            print('Dos')
        elif n==3 :
            print('Tres')
        elif n==4 :
            print('Cuatro')
        elif n==5 :
            print('Cinco')
        elif n==6 :
            print('Seis')
        elif n==7 :
            print('Siete')
        elif n==8 :
            print('Ocho')
        elif n==9 :
            print('Nueve')
        elif n==10 :
            print('Diez')
        elif n==11 :
            print('Once')
        elif n==12 :
            print('Doce')
        elif n==13 :
            print('Trece')
        elif n==14 :
            print('Catorce')
        elif n==15 :
            print('Quince')
    else :
        decena=n//10
        unidad = n-10*decena
        if unidad>0 : 
            if decena==1 :
                print('Diez', end=' ')
            elif decena==2 :
                print('Veinte', end=' ')
            elif decena==3 :
                print('Treinta', end=' ')
            elif decena==4 :
                print('Cuarenta', end=' ')
            elif decena==5 :
                print('Cincuenta', end=' ')
            elif decena==6 :
                print('Sesenta', end=' ')
            elif decena==7 :
                print('Setenta', end=' ')
            elif decena==8 :
                print('Ochenta', end=' ')
            else :
                print('Noventa', end=' ')
        else :
            if decena==2 :
                print('Veinte')
            elif decena==3 :
                print('Treinta')
            elif decena==4 :
                print('Cuarenta')
            elif decena==5 :
                print('Cincuenta')
            elif decena==6 :
                print('Sesenta')
            elif decena==7 :
                print('Setenta')
            elif decena==8 :
                print('Ochenta')
            else :
                print('Noventa')

        if unidad==1 :
            print('Uno')
        elif unidad==2 :
            print('Dos')
        elif unidad==3 :
            print('Tres')
        elif unidad==4 :
            print('Cuatro')
        elif unidad==5 :
            print('Cinco')
        elif unidad==6 :
            print('Seis')
        elif unidad==7 :
            print('Siete')
        elif unidad==8 :
            print('Ocho')
        elif unidad==9 :
            print('Nueve')     
else :
    print('Su número no cumple la condición.')
