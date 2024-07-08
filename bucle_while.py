# ### Nivel 1: Básico
# 1. **Contar hasta 10**:
#    Escribe un programa que utilice un bucle `while` para imprimir los números del 1 al 10.
# i=0
# while i < 10:
#     i=i+1
#     print(i)

# 2. **Suma de números**:
#    Escribe un programa que pida al usuario números hasta que el usuario ingrese un número negativo. 
# El programa debe sumar todos los números ingresados y mostrar el total al final.
# i = 0
# suma = 0
# while i >= 0:#mientras i sea menor que 5
#     i = int(input('Digita un numero: '))#se pediran numeros
#     if i > 0:#si i es mayor que 0
#         suma += i #suma el numero
# print(suma)
    


# ### Nivel 2: Intermedio
# 3. **Adivina el número**:
#    Escribe un programa que genere un número aleatorio entre 1 y 100. El programa debe permitir al usuario adivinar el número, 
# indicando si su suposición es muy alta, muy baja o correcta. El bucle `while` debe continuar hasta que el usuario adivine correctamente.
aleatorio = 0

while aleatorio in range(0,100):
    aleatorio = range
    print(aleatorio)



# 4. **Factorial de un número**:
#    Escribe un programa que calcule el factorial de un número dado por el usuario utilizando un bucle `while`.

# ### Nivel 3: Avanzado
# 5. **Serie de Fibonacci**:
#    Escribe un programa que imprima los primeros `n` números de la serie de Fibonacci, donde `n` es ingresado por el usuario. Utiliza un bucle `while` para generar la serie.

# 6. **Inversión de una cadena**:
#    Escribe un programa que invierta una cadena ingresada por el usuario utilizando un bucle `while`.

# ### Nivel 4: Experto
# 7. **Número primo**:
#    Escribe un programa que determine si un número ingresado por el usuario es primo utilizando un bucle `while`.

# 8. **Juego de adivinanzas**:
#    Escribe un programa que seleccione una palabra al azar de una lista de palabras. Luego, el programa debe permitir al usuario adivinar letras de la palabra. Si el usuario adivina una letra correctamente, la letra debe mostrarse en su posición correcta dentro de la palabra. El bucle `while` debe continuar hasta que el usuario haya adivinado todas las letras de la palabra.

# ### Nivel 5: Maestro
# 9. **Juego de la vida de Conway**:
#    Implementa una versión simplificada del Juego de la vida de Conway. Utiliza un bucle `while` para iterar a través de generaciones de la cuadrícula. Permite que el usuario especifique el tamaño de la cuadrícula y el número de generaciones a simular.

# 10. **Simulación de una máquina de Turing**:
#    Escribe un programa que simule una máquina de Turing simple. Permite que el usuario defina una cinta inicial, un conjunto de estados, y reglas de transición. Utiliza un bucle `while` para simular los pasos de la máquina hasta que llegue a un estado de aceptación o rechazo.
