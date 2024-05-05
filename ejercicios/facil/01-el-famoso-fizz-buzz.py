""" Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". """

# - A es multiplo de B cuando A es el resultado de multiplicar B por C
# - A = B * C -> A es multiplo de B

# Como saber si un num es multiplo de 3:
# - Si la suma de los numeros que lo componen es multiplo de 3 (divisible por 3)
# - Si es divisible por 3, es decir, el resultado es un numero natural entero

# Como saber si un num es multiplo de 5:
# - Si termina en 0 o en 5

# Como saber si un num es multiplo de 5 y de 3 a la vez:
# si un num es multiplo de 3 o de 5 tambien lo es de 15, ya que 3 y 5 son numeros primos entre si y su producto es 15

# Vamos a crear una funcion para cada comprobacion
def fizzbuzz(numero):
  if numero % 15 == 0:
    return 'fizzbuzz'
  elif numero % 5 == 0:
    return 'buzz'
  elif numero % 3 == 0:
    return 'fizz'
  else:
    return numero
  # el return sera fizz (mult de 3) o sera buzz (mult de 5) o sera fizzbuzz (mult de 3 y 5 a la vez) o sera el propio numero

# sabemos que hay que mostrar datos del 1 al 100, con lo cual podemos usar un bucle for con un rango de 1 a 100
for indice in range(1,101):
  print(fizzbuzz(indice))
