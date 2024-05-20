""" 
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva. 
"""
# El factorial de un numero n se define como
# n! = 1 * 2 * 3 * 4 * ... * (n - 1) * n
# hay una premisa que el factorial de 0! = 1

def recursive_factorial(number):
  # caso base que saldra de la recursividad, cuando el numero sea 0.
  if number == 0:
    return 1
  else:
    return number * recursive_factorial(number - 1)

result = recursive_factorial(5)
print(result) #24