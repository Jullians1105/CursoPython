def mifuncion ():#crear un bloque de codigo
    print('Mi primera funcion')


# mifuncion()#llamar a la funcion

# def imprimedato(nombre, apellido):#argumentos
#     print('nombre completo es:', nombre, apellido)
# #deben tener la misa cantidad en parametros que en argumentos
# imprimedato('Jullians', 'Amado')#parametros

#argumentos variables
def imprimedato(*nombre):#argumentos
    print('nombre completo es:', nombre)
#deben tener la misa cantidad en parametros que en argumentos
# imprimedato('Jullians', 'Amado', 'Gutierrez')#parametros
# con'*' genera una tupla, no se puede modificar los datos, pero si acceder a cada dato

def nombrecompleto (apellido, nombre):
    print(nombre, apellido)

# nombrecompleto(nombre= 'Jullians', apellido= 'Amado')

#**kwargs es como para usarlo como diccionario
def nombrecompleto2 (**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

# nombrecompleto2(nombre= 'Jullians', apellido= 'Amado')


#valor por defecto al argumento
def funcion (argumento='Jullians'):
    print(argumento)

# funcion('Amado')
# funcion()

#funcion como lista
def funcionlista (lista):
    for el in lista:
        print(el)

# funcionlista(['Jullians', 'Amado'])

def concatenanombres (lista):
    i= ''
    for el in lista:
        i = i + el +  ''
    return i

nombres = concatenanombres (['jullians', 'amado'])
# print(nombres)

#recusividad
def recursion (i):
    if(i< 1):
        return i
    print(i)
    recursion(i -1)

recursion(6)