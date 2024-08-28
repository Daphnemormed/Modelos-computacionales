# Considera las siguientes calificaciones:
# calif_1 = 10
#
# calif_2 = 7
#
# calif_3 = 4
#
# Calcula el promedio de las calificaciones considerando que:
#
# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total

calif_1 = 10
print(calif_1)
calif_2 = 7
print(calif_2)
calif_3 = 4
print(calif_3)

primera_nota = 15
print(primera_nota)
segunda_nota = 35
print(segunda_nota)
tercera_nota = 50
print(tercera_nota)

final1=(10*calif_1)/primera_nota
print('final1:', final1)
final2=(10*calif_2)/segunda_nota
print('final2:', final2)
final3=(10*calif_3)/tercera_nota
print('final3:', final3)

final1+final2+final3
print('promedio final:', final1+final2+final3)

# La siguiente matriz debe cumplir que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores. Crea un código para hacer las correcciones necesarias
# matriz = [ [1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13] ]

matriz = [ [1, 1, 1, 3],
      [2, 2, 2, 7],
      [3, 3, 3, 9],
      [4, 4, 4, 13] ]

list1=[1, 1, 1, 3]
if list1[3]==list1[0]+list1[1]+list1[2]:
    print('True')
else:
    list1[3]==list1[0]+list1[1]+list1[2]

list2=[2, 2, 2, 7]
if list2[3]==list2[0]+list2[1]+list2[2]:
    print('True')
else:
    print(list2[3]==list2[0]+list2[1]+list2[2])
list3=[3, 3, 3, 9]
if list3[3]==list3[0]+list3[1]+list3[2]:
    print('True')
else:
    print(list3[3]==list3[0]+list3[1]+list3[2])

list4=[4, 4, 4, 13]
if list4[3]==list4[0]+list4[1]+list4[2]:
    print('True')
else:
    print(list4[3]==list4[0]+list4[1]+list4[2])



