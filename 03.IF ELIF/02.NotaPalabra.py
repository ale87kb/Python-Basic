# Pedir una nota del 1 al 10 y mostrarla de la forma: Insuficiente (1-2), Regular (3-4), Bien (5-6), Muy bien (7-8), Sobresaliente (9-10).

nota=int(input('Escriba la nota del alumno (1-10): '))
if nota>=1 and nota<=10 :
    if nota>=1 and nota<=2 :
        print('Insuficiente')
    elif nota>=3 and nota<=4 :
        print('Regular')
    elif nota>=5 and nota<=6 :
        print('Bien')
    elif nota>=7 and nota<=8 :
        print('Muy bien')
    elif nota>=9 and nota<=10 :
        print('Sobresaliente')
else :
    print('Nota incorrecta.')
