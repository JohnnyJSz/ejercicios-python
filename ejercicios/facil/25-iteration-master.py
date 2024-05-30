""" 
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
"""

print('----')
# Manera numero 1 - bucle for usando range
for el in range(1,101):
  print(el)

print('----')
# Manera numero 2 - bucle while
num = 1
while num <= 100:
  print(num)
  num = num + 1

print('----')
# Manera numero 3 - funcion recursiva
def print_1_to_100(num):
  if num <= 100:
    print(num)
    print_1_to_100(num + 1)

print_1_to_100(1)
