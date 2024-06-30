#uso de if para condiciones 
#if 5 > 3:
    #print ("5 es mayor que 3");

#definicion de variables
Nombre= 'Jullians'
numero= 3167117358
#print(Nombre, numero)
#jugando con if y variables definidas
#if Nombre == 'Jullians' and numero != '3167117358':
    #print ("Es incorrecto")
#else:
    #print ("Es correcto")
#definiendo varias variables por separado 
a, b, c= 1, 2, 3
#print(a, b, c)
#definiendo varias variables como una sola
a1= b1= c1= 123
#print (a1, b1, c1)
#concatenacion
inicio= 'hola '
final= 'mundo'
#print (inicio+final)
#tipos de datos en python
#string
string = 'hola mundo,'
string1 = "hola mundo con comillas dobles,"

entero = 12345, #integer
decimales = 16.4, #float
complejos = 1j, # numeros complejos

#print(string, string1, entero, decimales, complejos)

#introduccion a listas 

lista = [1, 2, 3]
lista2 = lista.copy()#metodo de copia, antes de agregarle otro valor a la lista
lista.append(4) #metodo para agregar valores a la lista
#lista.clear()#metodo para eliminar valores de la lsita
#print (lista, lista2.count(1))#metodo count, para contar el valor que esta dentro de ()
#print (len(lista), len(lista2))#cuenta todos los elementos generales de la lista

Largolista = len(lista)
Largolista2 = len(lista2)

#print(Largolista, Largolista2)

#acceder a datos de arreglo o lista
lista3 =['Jullians', 'Amado', 1052]

#print (lista3[0])#para acceder a un elemento de la lista con []

#eliminar datos de una lista
#lista.pop() #eliminar ultimo dato de una lista
#lista.pop()
#print(lista)

#lista3.remove(1052)#eliminar valores especificos de una lista
#print(lista3)

lista2.reverse()#cambia el orden de la lista al contrario
#print(lista2)

lista.sort()#solo para valores del mismo tipo de dato, orden ascendente
#print(lista)    

#tuplas
tupla = ('hola', 'mundo', 'somos', 'tupla')
listatupla = list(tupla)#pasamos una tupla a una lista
listatupla.append('en vscode')
listatupla.reverse()
# print(tupla)
# print(tupla.count('hola'), tupla.index('somos'))
#count cuenta cuantas coincidencias encontro
#index dice la posicion de la palabra en especifico
# print(tupla[2])
# print(listatupla)
#print(len(listatupla), listatupla.index('somos'))

#rangos
rango = range (6)
# print(rango)#se usa en iteraciones

#diccionarios

diccinario = {
    "nombre": 'Jullians',
    "raza": 'hombre',
    "edad" : 19
}#creacion de un diccionario

# print(diccinario)
# print(diccinario['nombre']) #buscar valores especificos dentro del diccionario
# print(diccinario.get('edad'))#forma de bsucar valores mas eficaz
diccinario ['nombre'] = 'Jull' #editar valores de un diccionario
# print(len(diccinario)) 
diccinario['altura'] = 1.71#adicionar un valor
copiajull= diccinario.copy()#copiar un diccionario
copiajull1= dict(diccinario)#otra forma de copiar un diccionario
# print (diccinario)
diccinario.pop('altura')#elimina la propiedad y no lo que tiene
# hay que especificar en este .pop
# print(diccinario)
diccinario.popitem()#ultimo valor 
# print(diccinario)
del diccinario['raza']#otra forma de eliminar propiedades
# print(diccinario)
# print(diccinario, copiajull)
diccinario.clear()#eliminar todo el diccionario
# print(diccinario)
# print(copiajull1)


#diccionarios anidados
Gordo = {
    "Nombre" : 'Julian',
    "Edad" : 20
}

Flaco = {
    "Nombre" : 'Diego',
    "Edad" : 19,
}

Amigos1= {
    "Gordo" : Gordo,
    "Flaco" : Flaco,
}

# print(Amigos1)
#uso de dict para crear un diccionario
Perritos = dict (nombre = "Julian", Edad = 20)
print (Perritos)


#booleanos, verdadero o falso

verdadero = True
falso= False

print( verdadero, falso)

