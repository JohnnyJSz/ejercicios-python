""" 
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
- serie normal
  0, 1, 2, 3, 4, 5, 6, 7...
"""

def fibonacci_sequence():
  result = list()
  for i in range(0, 51):
    if i == 0 or i == 1:
      result.append(i)
    else:
      result.append(result[i - 1] + result[i - 2])
  return result

f_sequence = fibonacci_sequence()
print(', '.join(str(num) for num in f_sequence)) 
# para cada num en f_sequence castealo a str usando str(num)
# 'comprension de generador'