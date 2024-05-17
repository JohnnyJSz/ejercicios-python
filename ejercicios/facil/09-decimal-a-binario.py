""" 
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente. 
"""

def decimal_to_binary(number):
  # Para convertir de decimal a binario:
  # 1- dividir el numero entre 2
  # 2- Obtener el cociente de numeros enteros para la siguiente iteracion
  # 3- Obtener el resto, sera el digito binario.
  # 4- Repetir los pasos hasta que el cocinete sea igual a 0
  if number == 0:
    return ''

  cociente = number // 2
  resto = number % 2

  return decimal_to_binary(cociente) + str(resto)

# numero 25 -> binario 11001
print(decimal_to_binary(25))
# numero 13 -> binario 1101
print(decimal_to_binary(13))
# numero 174 -> binario 10101110
print(decimal_to_binary(174))