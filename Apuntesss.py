# Tarea anterior: matriz = [[1, 1, 1, 3],
#       [2, 2, 2, 7],
#       [3, 3, 3, 9],
#       [4, 4, 4, 13]]
# matriz[0][:3]
# sum(matriz[0][:3])
# for fila in range(4)
#     if matriz[fila][3] !=sum(matriz[fila][:3])
#         matriz[fila][3]=matriz[fila][:3]
# matriz

# Sentencia For (Para) con listas
promedio = 8
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for idx in numeros: # Para [variable local] en [lista]
    promedio += idx #Forma simplificada de promedio=promedio+idx
    print(str(idx)) #idx es el valor que va a tomar mientras se está haciendo la iteración
promedio /= len(numeros) #Al promedio lo estamos dividiendo sobre los elementos de la lista
print('el promedio es:', promedio)

#Otro ejemplo
numeros = [0, 2, 4, 5, 6, 8]
longitud = 0
for _ in numeros:
    longitud += 1
    print('se está ejecutando el for')
print('la longitud de la lista es:', longitud)# For al final es el número de iteraciones totales que hizo dicha función

# Enumerate (iterable, start = 0)
lista=['azul', 'verde', 56, ['2da lista']]
print(list(enumerate(lista)))

for idx, elemento in enumerate(lista):
    print('indice:', idx, 'elemento:', elemento)

for idx, elemento in enumerate(lista):
    print(lista[idx])
# o equivalentemente
for elemento in lista:
    print(elemento)

# Uso de continue y break
# break termina subitamente el for
# continue...

for idx in range(2,18):# OJO el último número de un rango no lo toma en cuenta
    print(idx)
    if idx % 2 == 0:
        print('es par')
        continue
        print('más código') # Ya no lo va a tomar en cuenta porque arriba de este código está el continue...
                            # si se cumple cierta condición, ignora el demás código (en este caso if) debajo de el
    else:
        print('es impar')

for letra in 'palabra':#Descompone los strings en sus caracteres
    print(letra)

# Funciones de entrada y salida de datos

# función de entrada de datos: input(); utilizamos para recibir info de teclado
string = input('introduce un número') #Siempre va a solicitarte info y la info que le metas la va a poner como cadenas
print('se recibió la cadena:', string)
print('con tipo de dato:', type(string))

numero = float(string)
print('el número es:', numero, 'con tipo de dato:', type(numero))

# Ejercicio 1
"""
Recibe por teclado un númeor entero n e imprime '123...n'
Ejemplo:
n=5
    devuelve '12345'
    
Rrestricciones: del 1 al 150
"""
numero_str = input('introduce un número del 1 al 150:')
n = int(numero_str)#número; int es para convertirlo en entero
print(list(range(1, n+1)))

# Ejercico 2
"""
Realiza un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar,
debe repetirse el proceso hasta que lo introduzca correctamente.
"""
numero_str = input('introduce un número impar:')

numero=int(numero_str)
    #verificar que el número es impar
if numero% 2 != 0:
    print('el número si es impar')

# Ejercicio 3
"""
Realiza un programa que sume todos los números enteros pares desde el 0 hasta un número que se introduzca por teclado.
Segerencia: Puedes utilizar las funciones sum() y range() para hacerlo más fácil.
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
"""
numero_str = input('introduce un número:')
numero = int(numero_str)#número; int es para convertirlo en entero
pares = range(0, numero, 2)
print('la suma de los pares hasta el número:', numero, 'es:', sum(pares))