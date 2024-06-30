# creacion de una clase con valores definidos
# class Usuaruio: 
#     nombre = 'Juan'
#     apellido = 'Feliz'
# usuario = Usuaruio()# se tiene que crear una variable y definirla con la clase para imprimir
# print(usuario.nombre, usuario.apellido) 


class Usuario: #definicion de la clase
    #init define los argumentos, y crear instancia para la clase
    #self se una para acceder a atributos y metodos de una clase de py
    def __init__(self, nombre, apellido):
        self.nombre= nombre #inicializa el atributo nombre
        self.apellido= apellido #inicializa atributo apellido
    def saludo (self):#se puede reutilizar el codigo
        print('hola mi nombre es: ', self.nombre, self.apellido)
usuario = Usuario('Jullians', 'Amado')
usuario1= Usuario('Mauricio', 'Gutierrez')

# usuario.saludo()#se llama el metodo como .metodo en la clase
# usuario1.saludo()

# class Usuario2: 
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido
#     def mostrar_informacion (self):# se creo un metodo
#         print(f'Nombre: {self.nombre}, Apellido: {self.apellido}')
#         #otra forma limpia y eficiente de construir cadenas con f' en el print
# usuario = Usuario2 ('Jullians', 'Amado')
# usuario1 = Usuario2 ('Mauricio', 'Gutierrez')

# usuario.mostrar_informacion()
# usuario1.mostrar_informacion()


#self, eliminar y modificar datos
class Usuario: #definicion de la clase
    #init define los argumentos, y crear instancia para la clase
    #self se una para acceder a atributos y metodos de una clase de py
    def __init__(self, nombre, apellido):
        self.nombre= nombre #inicializa el atributo nombre
        self.apellido= apellido #inicializa atributo apellido
    def saludo (self):#se puede reutilizar el codigo
        print('hola mi nombre es: ', self.nombre, self.apellido)
usuario = Usuario('Jullians', 'Amado')
# usuario1= Usuario('Mauricio', 'Gutierrez')

# usuario.saludo()#se llama el metodo como .metodo en la clase
# usuario.nombre = 'Julian'#editar nombre
# usuario.saludo ()
# # del usuario.nombre#eliminar nombre
# usuario.saludo()
# del usuario.nombre

#herencia

class Admin(Usuario):
    def super_saludo (self):
        print('Hola me llamo: ', self.nombre, self.apellido, 'Y soy admin')

# admin= Admin ('Super', 'Administrador')
# admin.saludo()
# admin.super_saludo()



class Animal:
    def __init__ (self, nombre, onomatopeya):
        self.nombre= nombre
        self.onomatopeya= onomatopeya
    def saludo1(self):
        print('Hola soy un', self.tipo ,  'y mi sonido es', self.onomatopeya)


class Gato(Animal):
    tipo= 'Gato'
    def __init__(self, nombre, onomatopeya):#al llamar init aqui se reemplaza del padre
        Animal.__init__(self, nombre, onomatopeya)#y al llamarlo aqui se obliga a reutilizarlo
        print('Hola soy un gato extendido')

class Perro(Animal):
    def __init__(self, nombre, onomatopeya):#tambien reemplaza
        super().__init__(nombre, onomatopeya)#otra forma de llamarlo
        print('Hola soy un perro instanciado')
    tipo = 'Perro'
gato= Gato ('Michi', 'Maullido')
gato.saludo1()

perro = Perro ('Lai', 'Ladrido')
perro.saludo1()

        

