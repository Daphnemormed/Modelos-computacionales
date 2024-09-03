# While
# Condiciones: condición inicial, condición de paro, condición de incremento

# Sentencia El se en bucle While
# Se encadena al while para ejecutar un bloque de código una vez que la condición
# ya no devuelve True (normalmente al final).
lista = ['chocolate', 'tristeza', 'cualquiera', 'naranjas', 'azul', 'parque']
indice = -3
while lista[indice] != 'cualquiera': # Condición de paro porque nos aseguramos de que es Falso
    print(indice, lista[indice]) # Condición inicial
    indice += 1 # Condición de incremento
else:
    print('se cumplió la condición, ya me quiero mimir')

# Ejemplo donde no se cumple la condición de paro
# idx = 0
# while True: -> Aquí no se cumple
#     idx *= 2
#     print(idx)
# else:
#     print('salio')

# Ejemplo con brake
c = 0 # Condición inicial
while c <= 5: # Condición de paro
    c += 1
    print("c vale", c)
    if c == 4:
        print("rompemos el bucle cuando c vale", c)
        continue
else:
    print("Se ha completado toda la iteración y c vale", c)

# Funciones
# Son fragmentos de código que se pueden ejecutar múltiples veces.
# Pueden recibir y devolver información para comunicarse con el proceso principal

# Definición y llamada
def saludar():
    print("Hola! Este print se llama desde la función saludar()")

saludar()

def escribir_tabla_del_5():
    for i in range(10):
        # print("5 * {} = {}".format(i, 1*5))
        print('5 *', i+1, '=', 5*(i+1))

# escribir_tabla_del_5()

# formas de usar el print
val = 10
print('5 *', val+1, '=', 5*(val+1))
# Separa por comas todas las variables que quiero que imprima
print('5 * {} = {}'.format(10,50))
print('5 * {1} = {0}'.format(10,50)) # Cambia los valores "10" y "50" de lugar
print('5 * {0} = {1}'.format(10,50))
print(f'5 * {val} = {5*val}')
# f=format: reconoce las llaves y sabe que ahí debe de poner algo

# Variables globales vs variables locales
# Una variable declarada en una función no existe en la función principal:
def test():
    n = 10
    print('n=', n)
    return n

n = test()
print('globalmente n =', n)