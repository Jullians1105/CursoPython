# uso de if 
# if 2 < 5:
    # print('2 es menor que 5')

#dos variables iguales con a==b
#a > b
#a < b
#a != b
#a <= b
#a >= b

# if 2 == 2:
    # print('2 es igual a 2')

# if 2 == 3:
    # print('2 ]es igual a 3')

# if 2 > 5:
    # print('2 es mayor que 5')

# if 5 > 2:
    # print('5 es mayor que 2')

# if 2 != 2:
    # print('2 es distinto a 2')

# if 3 != 2:
    # print('3 es distinto a 2')

# if 3 >= 3:
    # print('3 es mayor o igual a 2')

# if 3 <= 3:
    # print('3 es menor o igual a 3')    


#if, else, elif

# if 2 == 5:
#     print('lala')
# elif 2 == 5:# se ejecuta solo si if es falso
#     print('2 menos a 5 en elif')
# elif 2 != 5:#se pueden traer todas las veces que queira
#     print('2 es distinto de 5 segundo elif')
# else:
#     print('me imprimo si lo anterior es falso')

# if 2 == 5:
#     print('lala')
# else:
#     print('me imprimo si lo anterior es falso2')


#if cortos y ternarios
# if 2 < 5: print('if de una linea')
# print('cuando sea vddero') if 5 > 2 else print('cuando es falso') #operador ternario

#and y or
#and, solo cuando las dos son verdaderas
# if 2 < 5 and 5 > 2:
    # print('ambas verdadero')

# if 2 < 5 and 5 < 2:
    # print('una falsa')#no ejecuta

#or, alguna de las dos son verdaderas
# if 2 < 5 or 5 < 2:
    # print('una de las dos es verdadero')

#imput y primer juego

#bucles

#while
i = 0

# while i < 5:
#     print (i)
#     i = i + 1

#detenerla cuando cumpla la condicion del if 
# while i < 5:
#     print (i)
#     if i == 3:
#         break
#     i = i + 1
#continue sirve para saltar el elemento de condicion
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print (i)

#for# acceder elementos de un arreglo
# usuarios = ['Jullians', 'Felipe', 'Roberto', 'Nicolas']
# for usuario in usuarios:
#     print(usuario)#llamar a todos los elementos de la lista

#acceder a caracteres 
# usuario = 'Jullians'
# for c in usuario:
#     print(c)
# usuarios = ['Jullians', 'Felipe', 'Roberto', 'Nicolas']
# for usuario in usuarios:
#     if usuario == 'Roberto':
#         break#no imprime despues de encontrar a roberto
#     print(usuario)

#uso de rango en for
# for x in range (3, 30, 3):#en z es el numero de incremento
#     print(x)
# else:#cuando acaba toda la ejecucion
#     print('hemos terminado')

# usuarios = ['Jullians', 'Felipe', 'Roberto', 'Nicolas']
# edades =[19, 21, 20, 20]
# for usuario in usuarios:
#     for edad in edades:
#         print (usuario, edad)