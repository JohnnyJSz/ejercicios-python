""" 
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_a_prime_number(number):
  if number <= 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      return False
    
  return True

for i in range(1, 101):
  if is_a_prime_number(i):
    print(i)