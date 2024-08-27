# Diccionarios
diccionario1 = {'llave1': 'lobo', 'llave2': -82.654, 34: 'cosa', 'llave4': [2, 3, 4]}
print('diccionario1', diccionario1)

# Pop
diccionario1.pop('llave4')
print('diccionario1 sin llave4', diccionario1)

# Get
diccionario1.get('llave1') # Obtener el valor asociado con una clave específica
print('valor asociado a la llave1:', diccionario1.get('llave1'))

# Copy
diccionario1.copy()
print(diccionario1.copy())
print('Diccionario1 copiado:', diccionario1.copy(), 'es de tipo', type(diccionario1.copy()))

# Keys
diccionario2 = {'llave1': 'caracol', 'llave2': 'chocolate', 'llave3': 'planta', 'llave4': 8}
diccionario2.keys()
print(diccionario2.keys())

# Items
diccionario1.items()
diccionario2.items()
print('Items de diccionario1:', diccionario1.items(), 'y items de diccionario2:', diccionario2.items())

# Clear
diccionario1.clear()
print('Diccionario1 vacío:', diccionario1.clear())

# Fromkeys
keys = ['a', 'b', 'c']
value = ['helado', 'comida', 'papas']
diccionario2.fromkeys(keys, value)
print('Diccionario2 con keys nuevas y nuevos valores:', diccionario2.fromkeys(keys, value))
# Crea un nuevo diccionario con las claves proporcionadas y un valor predeterminado asociado a cada clave.

# Pop item
diccionario2 = {'llave1': 'caracol', 'llave2': 'chocolate', 'llave3': 'planta', 'llave4': 8}
diccionario2.popitem()
print('ejemplo de popitem del diccionario2:', diccionario2.popitem())
# Eliminar y devolver un par clave-valor del diccionario.

# Setdefault
diccionario2.setdefault('llave2') # devuelve el valor asociado a esa clave sin modificar el diccionario.
print('El valor de la llave2 es:', diccionario2.setdefault('llave2'))

# Update
diccionario3 = {'llave1':'a', 'llave2':'b', 'llave3':'c'}
diccionario2.update(diccionario3) # Actualiza el valor de la clave con el valor dado en el diccionario que se utilizó para actualizar
print('Actualizamos el diccionario2 con el diccionario3:', diccionario2)


# Values
diccionario2.values() # Obtener una vista de todos los valores en el diccionario.
print('valores del diccionario2:', diccionario2.values())
