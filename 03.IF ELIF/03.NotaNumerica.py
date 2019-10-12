# Pedir una nota en palabra y pasarla a numérica. Ejemplo: 'uno' y devuelve 1, 'seis' y devuelve 6, 'diez' y devuelve 10.

nota=input('Escriba la nota en palabra: ')
if nota=='uno' or nota=='Uno' or nota=='UNO' :
    print('1')
elif nota=='dos' or nota=='Dos' or nota=='DOS' :
    print('2')
elif nota=='tres' or nota=='Tres' or nota=='TRES' :
    print('3')
elif nota=='cuatro' or nota=='Cuatro' or nota=='CUATRO' :
    print('4')
elif nota=='cinco' or nota=='Cinco' or nota=='CINCO' :
    print('5')
elif nota=='seis' or nota=='Seis' or nota=='SEIS' :
    print('6')
elif nota=='siete' or nota=='Siete' or nota=='SIETE' :
    print('7')
elif nota=='ocho' or nota=='Ocho' or nota=='OCHO' :
    print('8')
elif nota=='nueve' or nota=='Nueve' or nota=='NUEVE' :
    print('9')
elif nota=='diez' or nota=='Diez' or nota=='DIEZ' :
    print('10')
else :
    print('Nota inválida.')
