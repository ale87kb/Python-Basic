# Pedir la edad y si esta es menor a 5 o mayor a 100 que diga que es incorrecta y vuelva a pedirla, miestras que si es correcta, la imprima por pantalla.

edad=int(input('Ingrese la edad: '))
while edad<5 or edad>100:
    print('Edad incorrecta.')
    edad=int(input('Ingrese la edad: '))
print('Edad: '+str(edad))
