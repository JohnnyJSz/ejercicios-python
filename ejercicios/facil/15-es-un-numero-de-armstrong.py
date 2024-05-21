""" 
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto. 
"""

# Un numero es considerado numero armstrong cuando es igual a la suma de sus
# propios digitos cada uno elevado a la potencia del numero de digitos.
# Este concepto se aplica a los numeros en base 10.
# Ejemplo:
# 153 -> 3 digitos -> 1**3 + 5**3 + 3**3 = 153
# 1634 -> 4 digitos -> 1**4 + 6**4 + 3**4 + 4**4 = 1634

def is_number_armstrong(number):
  # Comprobar cuantos digitos tiene el numero
  str_number = str(number)
  num_of_digits = len(str_number)

  result = 0
  for digit in str_number:
    result = result + int(digit) ** num_of_digits

  if result == number:
    return True
  else:
    return False


# Numeros Armstrong
number1 = 153
number2 = 1634
number3 = 93084

# Numeros NO Armstrong
number4 = 146
number5 = 95432
number5 = 25

result1 = is_number_armstrong(number1)
result2 = is_number_armstrong(number2)
result3 = is_number_armstrong(number3)
result4 = is_number_armstrong(number4)
result5 = is_number_armstrong(number5)

print(f'Es el numero {number1} considerado numero Armstrong?: {result1}')
print(f'Es el numero {number2} considerado numero Armstrong?: {result2}')
print(f'Es el numero {number3} considerado numero Armstrong?: {result3}')
print(f'Es el numero {number4} considerado numero Armstrong?: {result4}')
print(f'Es el numero {number5} considerado numero Armstrong?: {result5}')
