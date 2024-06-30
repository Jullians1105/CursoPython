# dato = input('Ingrese dato: ')#pedir datos

# lista = ['hola', 'mundo', 'perro', 'gato']

# if lista.count(dato) > 0:
#     print('El dato existe,')
# else:
#     print('El dato no existe', dato)


# dato1 = input('Ingrese primer numero: ')
# try:#si dato1 es un numero, se guarda como entero
#     dato1 = int(dato1)
# except:#de lo contrario se guardara como una palabra
#     dato1 = 'Jullians'

# dato2 = input('Ingrese segundo numero: ')
# try:#si dato2 es un numero, se guarda como entero
#     dato2= int(dato2)
# except:#de lo contrario se guardara como una palabra
#     dato2= 'Amado'

# if dato1 == 'Jullians' or dato2 == 'Amado':
#     print('ingresaste mal un dato, solo con numeros')
# else:
#     print(dato1+dato2)
# primero = int (dato1)#pasar datos a enteros
# segundo = int (dato2)#pasar datos a enteros
# print(primero+segundo)


#modelo de validacion
dato1 = input('Ingrese primer numero: ')
try:#si dato1 es un numero, se guarda como entero
    dato1 = int(dato1)
except:#de lo contrario se guardara como una palabra
    dato1 = 'Jullians'
if dato1 == 'Jullians':
    print('no es valido')
    exit()
dato2 = input('Ingrese segundo numero: ')
try:#si dato2 es un numero, se guarda como entero
    dato2= int(dato2)
except:#de lo contrario se guardara como una palabra
    dato2= 'Amado'
if dato2 == 'Amado':
    print('no es valido')
    exit()
else:
    print(dato1+dato2)

simbolo = input('Ingresa la operacion: , +, -, *, /: ')

if simbolo == '+':
    print('la respuesta es ', dato1+dato2)
elif simbolo == '-':
    print('la respuesta es ', dato1-dato2)
elif simbolo == '*':
    print('la respuesta es ', dato1*dato2)
elif simbolo =='/':
    print ('la respuesta es ', dato1/dato2)

else:
    print('el simbolo no es correcto') 



