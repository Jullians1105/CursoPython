# [python]

# ¡Por supuesto! Aquí tienes los ejercicios sin resolver:

# ### Nivel Fácil

# 1. **Imprimir números del 1 al 10**:
#    - Escribe un bucle `for` que imprima los números del 1 al 10.

# for i in range(0,10):#imprime del 0 al 10 usando el rango
#     print(i)

# 2. **Imprimir cada carácter de una cadena**:
#    - Escribe un bucle `for` que imprima cada letra de la cadena `'Hola'`.
# cadena = "'Hola'"
# for i in cadena:#digamos que i es "cada", por cada letra en cadena, imprime letra a letra
#     print(i)
# 3. **Sumar los elementos de una lista**:
#    - Escribe un bucle `for` que sume los elementos de la lista `[1, 2, 3, 4, 5]` y luego imprima la suma.
# lista = [ 1,2,3,4,5]
# suma = 0
# for i in lista:
#     suma= suma+i
#     print(suma)    
# ### Nivel Intermedio

# 4. **Imprimir solo los números pares del 1 al 20**:
#    - Escribe un bucle `for` que imprima solo los números pares del 1 al 20.
# for i in range (1,20,2):
#     print(i)

# for i in range (1,21):
#     if i%2 == 0:
#         print(i)
    
# 5. **Multiplicar los elementos de una lista por 2**:
#    - Escribe un bucle `for` que multiplique cada elemento de la lista `[1, 2, 3, 4, 5]` por 2 y luego imprima los resultados.

# lista = [ 1,2,3,4,5]
# for multi in lista:
#     multi = (multi) * 2
#     print(multi)

# 6. **Imprimir los elementos de una lista en orden inverso**:
#    - Escribe un bucle `for` que imprima los elementos de la lista `[1, 2, 3, 4, 5]` en orden inverso.

# lista = [ 1,2,3,4,5]
# lista.reverse()
# for inverse in lista:
#     print(inverse)

# lista = [1,2,3,4,5]
# for inverse in reversed (lista):
#     print(inverse)

# ### Nivel Avanzado

# 7. **Contar las vocales en una cadena**:
#    - Escribe un bucle `for` que cuente cuántas vocales hay en la cadena `'Hola, ¿cómo estás?'` y luego imprima el conteo total.

cadena = 'Hola, ¿cómo estás?'
vocales = 'aeiouáéíóúAEIOUÁÉÍÓU'
count_vocales = 0
for i in cadena:
    if i in vocales: 
        count_vocales += 1
        
        
print(count_vocales)



# 8. **Generar una lista de los primeros 10 números cuadrados**:
#    - Escribe un bucle `for` que genere una lista de los primeros 10 números cuadrados (1, 4, 9, ... 100).

# 9. **Encontrar el número máximo en una lista**:
#    - Escribe un bucle `for` que encuentre el número máximo en la lista `[5, 3, 8, 6, 7, 2]` y luego imprima el número máximo.

# 10. **Filtrar los números mayores que 5 en una lista**:
#     - Escribe un bucle `for` que recorra la lista `[3, 6, 8, 2, 9, 1, 5]` y cree una nueva lista que contenga solo los números mayores que 5.
