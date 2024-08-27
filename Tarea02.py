# Determinar si los tipos de datos range cumplen:
# mutabilidad
# suma
# producto por un entero
# slicing
# convertir a lista o tupla
# función len

rango1 = range(5)
print('ejemplo de rango 1:', rango1, 'rango1 es de tipo:', type(rango1))
rango2 = range(9)
print('ejemplo de rango 2:', rango2, 'rango2 es de tipo:', type(rango2))

# Mutabilidad
# rango1[5] = 'helado' no es mutable: 'range' object does not support item assignment

# Suma
# rango1, rango2 = range(5), range(9)
# print('suma de rangos:', rango1 + rango2)
# No se puede: unsupported operand type(s) for +: 'range' and 'range'

# Producto por un entero
# print('multiplicando rango por un entero:', rango1*4)
# No se puede: unsupported operand type(s) for *: 'range' and 'int'

# Slicing
print('aplicando slicing:', rango1[0])# slicing de un elemento
print('aplicando slicing con números negativos:', rango1[-4:-1])# slicing de más elementos

# Conversión
print('convirtiendo rango a lista:', list(rango1), 'tiene tipo:', type(list(rango1)))
print('convirtiendo rango a tupla:', tuple(rango1), 'tiene tipo:', type(tuple(rango1)))

# Función len
# print('aplicando la función len:', len(rango1+rango2))
# No se puede: unsupported operand type(s) for +: 'range' and 'range'
