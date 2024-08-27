list = [1, 2, 3]
print  ('list =', list)

# Append para añadir un item
list.append(4)
print (list)

# Extend*
iterable = [5, 6, 7]
list.extend(iterable)
print(list)

# Insert
list.insert(4, 4.5)
print(list)

# Remove
list.remove(1)
print(list)

# Pop*
list.pop(3)
print(list)

# Clear para dejar vacía la lista
list.clear()
print(list)

# Index
list2 = [1, 2, 3, 4]
print(list2)
list2.index(3)
print(list2.index(3))

# Count para contar cuántas veces aparece un elemento específico en la lista
list3 = [1, 2, 4, 8, 1, 2, 3, 5, 8, 9, 6, 4, 2, 3, 7, 8, 1]
print(list3)
list3.count(8)
print(list3.count(8))

# Sort para ordenar ls elementos de la lista
list3.sort()
print(list3)

# Reverse para ordenarlos al revés
list3.reverse()
print(list3)

# Copy
list3.copy()
print(list3)