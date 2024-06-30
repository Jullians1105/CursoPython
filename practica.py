# Comentarios

#1. suma de dos numeros

# numero1 = input ('Escribe el primer numero: ')
# try:
#     numero1 = int(numero1)
# except:
#     numero1 = 'numero1'
    
# numero2 = input ('Escribe el segundo numero: ')
# try:
#     numero2 = int(numero2)
# except:
#     numero2 = 'numero2'

# if numero1 == 'numero1' or numero2 == 'numero2':
#     print('ingresaste mal un dato')
# else:
#     print ('El resultado es:',  numero1 + numero2)
# exit()

#Variables

#2. crear variable para nombre y edad e intercambiarlo sin otra variable

nombre = 'Jullians'
edad= 19
# print('Antes del intercambio', nombre,  edad)
nombre, edad = edad, nombre
# print('Despues del intercambio', nombre,  edad)

# Multiples variables

#3. con 3 variables para 1, 2, 3, imprimir cada una de ellas

a, b, c= 1, 2, 3
# print('Antes del intercambio:', a, b, c)

#3. mismo ejercicio, pero (a -> b, b -> c, c -> a)
a, b, c = b, c, a
# print('Despues del intercambio:', a, b, c)

# Concatenacion

#4. concatenar dos cadenas de texto e imprimir

oracion1 = 'El curso de python'
oracion2 = ' es muy bueno'

# print(f'{oracion1}{oracion2}')#otra forma de concatenar

oracion3= 'Llevo 1 semana, y ahora un numero cualqueira '
# int= 5
# print(f'{oracion3} {int}' )


#

# Tipo de datos 

#1. convierte una cadena que tiene un entero y hacer suma con otro numero
# lista = ['Juan', 'Felipe', 5]
# # print(lista)
# num= input ('Segundo numero: ')
# try:
#     num = int(num)

#     suma = lista[2]+ num
#     # print(suma)
# except: 
#     print('Ingrese un numero')

#2. Programa que reciba un numero del usuario, lo convierta en flotante y muestre la mitad
# num2= input('dame un numero: ')
# try:
#     num2=float(num2)
#     mitad= num2/2
    # print(f'la mitad de {num2} es {mitad}')
# except:
#     print('Ingresa bien los datos')

# Intro a listas

#1. Crear una lista de 5 elementos y mostrar el tercer elemento
listaa= ['juan', 'mateo', 'sebastian', 'camilo', 'sara']
# print(listaa[2])

#2. Añadir nuevo elemento al final de la lista y mostrarla completa   

listaa.append('santiago')
# print(listaa)

# Contando elementos y calculando elementos de una lista

#1. Crea una lista de # y muestra la suma de todos los elementos
listanum= [1,2,3,4,5]
suma= sum(listanum)
# print(suma)
# #2. CUenta cuantas veces aparece un elemento en una lista dada  
lista4 = [7, 7, 7, 7, 6, 5, 3, 7, 1]
# print(lista4.count(7))

#Accediento a elementos de las listas

#1. Accede al primer y ultimo elemento de una lista e imprimirlos
lista5 = [10, 1, 2, 7, 6, 5, 3, 7, 1]
# print(lista5[0], lista5[8], lista5)#se puede usar -1 para el ultimo valor, si cambia la longitud
#2. Cambiar el valor del segundo elemento de una lista e imprime la lista actualizada

lista5[1]= 8
# print(lista5)

#Accediendo a elementos de las listas

#1. Acceder al primer y ultimo elemento de una lista e imprimelos

# lista6 = ['Juan', 'Felipe', 'sebastian', 'santiago']
# print(lista6[0], lista6[3])

#2. Cambia el valor del segundo elemento de una lista e imprime la lista actualizada
# lista6 [2]= 'Samuel'
# print(lista6)

#Eliminando elementos de una lista

#1. Eliminar tercer elemento de una lista e imprime la lista
# lista6 = ['Juan', 'Felipe', 'sebastian', 'santiago']
# lista6.remove('santiago')
# print(lista6)
#2. Usa el meotodo 'pop' para eliminar y mostrar el ultimo elemento de la lista
# lista6.pop()
# print(lista6)
#Reverse y sort
 
#1. ordena una lista de numeros en orden ascendeten y descendente
# lista7 = [7, 7, 7, 7, 6, 5, 3, 7, 1]
# lista7.sort()
# print(lista7)
# lista7.sort(reverse=True)#otra forma de ordenarlo de forma descendente
# print(lista7)

#2. iniverte el orden de una lista y muestrala
# lista8 = [7, 7, 7, 7, 6, 5, 3, 7, 1]
# lista8.reverse()
# print(lista8)
#Tuplas

#1. Crea una tupla con 4 elementos y muestra el segundo
# tupla = ('Hola', 'Mundo', 'De', 'Python')
# print(tupla[1])
#2. Convierte una lista en una tupla y viceversa
# tuplalista = tuple(lista8)
# print(tuplalista)

#Rangue

#1. Crea una lista de números del 0 al 9 usando `range`
# rangoo = range(0,10)
# print(list(rangoo))
#2. Genera una lista de números pares del 2 al 20 usando `range`
rangooo = range(0,10,2)#el valor de z define que sea par
# print(list(rangooo))
#Introduccion a Diccionarios

#1. Crea un diccionario con 3 pares clave-valor e imprime una de las claves

diccionario = {
    "nombre": 'Jullians',
    "edad": '19',
    "estatura": 1.71
}
# print(diccionario['estatura'])

#2. Agrega un nuevo par clave-valor al diccionario y muestra el diccionario completo
diccionario["carrera"] = 'ing software' #agregar un valor a un diccionario
# print(diccionario)

#Diccionarios anidados y constructor `dict`

#1.Crea un diccionario anidado y accede a un valor dentro del diccionario interno

Perro1 = {
    "nombre": 'Mateo',
    "edad": 10,
    "color": 'Blanco'
}
Perro2 = {
    "nombre": 'Cliford',
    "edad": 15,
    "color": 'Blanco'    
}
Perro3 = {
    "nombre": 'Lyon',
    "edad": 2,
    "color": 'Dorado'
}

Perros = {
    "Mateo": Perro1,
    "Cliford": Perro2,
    "Lyon" : Perro3
}

# print(Perros['Lyon'])

#2. Usa el constructor `dict` para crear un diccionario y mostrarlo

carros = dict(nombre = 'Ferrari', color= 'Negro')
# print(carros)

#Booleanos

#1. Crea una variable booleana y usa una condición `if` para mostrar un mensaje si es `True`

# verdadero = True
# falso = False

# if  2+2 == 4:
#     print(verdadero)
# else:
#     print(falso)

#2. Escribe un programa que reciba dos números y muestre `True` si el primero es mayor que el segundo

# num1 = input ('Ingrese un numero: ')
# num2 = input ('Ingrese el segundo numero: ')

# if num1 > num2:
#     print(verdadero)
# else:
#     print(falso)

# If y Condiciones

# 1. Escribe un programa que determine si un número es positivo, negativo o cero.
# num3 = input('Escribe un numero: ')
# num3 = int(num3)
# if num3 > 0:
#     print('Es positivo')
# elif num3 == 0:
#     print('Es igual a cero')
# elif num3 < 0:
#     print('Es negativo')

# 2. Crea un programa que verifique si un número es par o impar.
# num5 = input('Escribe un numero: ')
# num5 = int(num5)

# par= num5%2

# if par == 0:
#     print('Es un numero par')
# else:
#     print('Es inpar')

# If, elif y else

# 1. Escribe un programa que asigne una calificación (A, B, C, etc.) basada en una puntuación.

# puntuacion = input('Dime tu nota: ')
# puntuacion = float(puntuacion)

# if puntuacion == 5:
#     print('Excelente, la nota es de ', puntuacion)
# elif puntuacion > 3 and puntuacion <= 5:
#     print('Puntuacion regular, la nota es de ', puntuacion)
# elif puntuacion > 0 and puntuacion < 3:
#     print('Mala puntiacion, la nota es de ', puntuacion)



# 2. Crea un programa que determine la estación del año basada en un mes dado.

# estacion = int(input('Digita un mes del año'))


#invierno de diciembre a marzo, entre 12 o 3
#primavera de marzo a junio, entre 3 o 6
#verano de junio a septiembre, entre 6 o 9
#otoño de septiembre a diciembre, entre 9 o 12

# if estacion in [12, 1, 2]: #otra forma de anidar if
#     print('Es la estacion de invierno')
# elif estacion in [3, 4, 5]:
#     print('Es la estacion de primavera')
# elif estacion in [6, 7, 8]:
#     print('Es la estacion de verano')
# elif estacion in [9, 10, 11]:
#     print('Es la estacion de otoño')
    

#  If cortos y terniarios

# 1. Usa una expresión ternaria para determinar si una persona es mayor de edad.

# edad = int(input('Escribe tu edad'))
# print('Es mayor de edad' if edad >= 18 else 'Es menor de edad')

# 2. Escribe una expresión corta que asigne `True` o `False` a una variable basada en una condición.

# if 2+2 != 4:
#     print(True)
# else:
#     print(False)

#  And y or

# 1. Crea un programa que verifique si un número está dentro de un rango específico usando `and`.
# rango = int(input('Digita un numero: '))

# if rango >= 0 and rango <= 10:
#     print('Esta dentro del rango')
# else:
#     print('No esta en el rango')

# 2. Usa `or` para determinar si una variable es `None` o una cadena vacía.

# cadena = input('Escribe algo: ')
# if len(cadena) == 0:
#     print('Esta vacio')
# else:
#     print('None')

#   Ejercicios

#  Calculadora que suma

# 1. Escribe un programa que sume dos números ingresados por el usuario.

# num1 = int(input('Digita el primer numero: '))
# num2 = int(input('Digita el segundo numero: '))

# print('El resultado es ',num1 + num2)

# 2. Mejora el programa para que valide que los datos ingresados sean números.

# num1 = (input('Digita el primer numero: '))
# num2 = (input('Digita el segundo numero: '))

# try: 
#     num1 = int(num1); num2 = int(num2)
# except:
#     num1 = 'num1'; num2 = 'num2'
    
# if num1 == 'num1': 
#     print('Escribe correctamente')    
# if num2 == 'num2':
#     print('Escribe correctamente')

# print('El resultado es: ', num1+num2)

#  Moviendo la validación

# 1. Escribe una función que valide si una entrada es un número y úsala en el programa de la calculadora.

# num1 = (input('Digita el primer numero: '))
# num2 = (input('Digita el segundo numero: '))

# try: 
#     num1 = int(num1); num2 = int(num2)
# except:
#     num1 = 'num1'; num2 = 'num2'
    
# if num1 == 'num1': 
#     print('Escribe correctamente')    
# if num2 == 'num2':
#     print('Escribe correctamente')

# print('El resultado es: ', num1+num2)

# 2. Refactoriza el programa para mover toda la lógica de validación a funciones separadas.   ///

#  Agregando más operaciones

# 1. Extiende la calculadora para soportar resta, multiplicación y división.

# num1 = (input('Digita el primer numero: '))
# num2 = (input('Digita el segundo numero: '))

# operacion = input ('Escoje la operacion que quieres realizar, + - * /: ')

# try: 
#     num1 = float(num1); num2 = float(num2)
# except:
#     num1 = 'num1'; num2 = 'num2'
    
# if num1 == 'num1': 
#     print('Escribe correctamente')    
# if num2 == 'num2':
#     print('Escribe correctamente')

# if operacion == '+' : print('El resultado es: ', num1+num2)
# elif operacion == '-': print('El resultado es: ', num1-num2)

# elif operacion == '/' and num2==0: print('No se puede dividir entre 0')
# elif operacion == '*': print('El resultado es: ', num1*num2)
# else : print('Esta mal la operacion'); print(operacion == '/'); print('El resultado es: ', num1/num2)
# 2. Maneja los casos en los que la división sea por cero.
# hice la implementacion en el codigo de arriba
#   Control de Flujo, Bucles
#  While

# 1. Escribe un programa que cuente del 1 al 10 usando un bucle `while`.

# x= 0
# while x < 11:
#     print(x)
#     x=x+1

# 2. Crea un programa que pida números al usuario hasta que ingrese un número negativo.

# x= int(input('digita un numero:')) #pido un numero

# if x >= 0: #si el numero es mayor o igual a cero
#     while x >= 0: #mientras el numero sea mayor o igual a 0 
#         print(x) #imprimira el numero que se digito
#         x= int(input('digita un numero:'))#hasta que el numero sea negativo, ahi acabara el ciclo

        
        

#  While: break y continue

# 1. Usa `break` para salir de un bucle `while` cuando se cumpla una condición específica.

# x1= int(input('escribe un numero: '))#pido un numero

# while x1 < 10 and x1 >0:# mientras el numero sea menor a 10 y mayor que 0
#     print(x1)#lo imprimimos
#     if x1+2 ==7:#y si la suma del numero +2 da igual a 7
#         print('Es correcto')#dira que es correcto
#         break#y dejara de ejecutarse
#     else:#de lo contrario
#         x1= int(input('escribe un numero: '))#volvera a pedir un numero
# 2. Utiliza `continue` para saltar una iteración específica en un bucle `while`.

x2= 2#defino x2

while x2 < 7:# mientras que x2 sea menor que 7
    x2 = x2+1#se sumara uno hasta llegar a 7
    if x2 ==5:#y si x2 es igual a 5
        continue#se lo saltara 
    print(x2)#e imprimira los valores hasta terminar hasta el 7

#  For

# 1. Escribe un bucle `for` que imprima cada letra de una cadena.
# 2. Crea un bucle `for` que itere sobre una lista y sume sus elementos.

#  Funciones

# 1. Define una función que reciba dos números y devuelva su suma.
# 2. Escribe una función que determine si un número es primo.

#  Recursividad

# 1. Escribe una función recursiva para calcular el factorial de un número.
# 2. Crea una función recursiva que imprima los números de una lista en orden inverso.

#   Objetos, clases y herencias

#  Objetos y clases

# 1. Define una clase `Persona` con atributos `nombre` y `edad`.
# 2. Crea una instancia de la clase `Persona` y muestra sus atributos.

#  Métodos

# 1. Añade un método `presentarse` a la clase `Persona` que imprima una presentación.
# 2. Crea un método que incremente la edad de la persona en un año.

#  Self, eliminar propiedades y objetos

# 1. Muestra el uso de `self` en los métodos de la clase.
# 2. Elimina un atributo de un objeto y muestra cómo manejar la excepción si se intenta acceder a él.

#  Herencia

# 1. Define una clase `Empleado` que herede de `Persona` e incluya un atributo `salario`.
# 2. Crea una instancia de `Empleado` y muestra sus atributos, incluyendo los heredados.

#  Ejercicio de herencia

# 1. Escribe una clase `Gerente` que herede de `Empleado` y añada un método para gestionar empleados.
# 2. Crea una lista de empleados y permite al `Gerente` gestionar (agregar/eliminar) empleados en la lista.

#  Expandiendo método `__init__` del padre

# 1. Modifica el método `__init__` de `Empleado` para aceptar un nuevo atributo `departamento`.
# 2. Asegúrate de llamar al `__init__` del padre para no sobrescribir la inicialización de `Persona`.


