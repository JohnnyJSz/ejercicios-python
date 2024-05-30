""" 
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes
  de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes
  de los dos array.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente. 
"""

def function(array1, array2, boolean):
  array = []
  if boolean:
    # busca y devuelve los elementos comunes de los dos arrays
    for element in array2:
      if element in array1:
        array.append(element)
    return array
  else:
    # busca y devuelve los elementos no comunes de los dos arrays
    for element in array2:
      if element not in array1:
        array.append(element)
    for element in array1:
      if element not in array2:
        array.append(element)
    return array
  
array1 = [1,2,3,4,5]
array2 = [3,6,1,7,5]
# Elementos comunes -> 3, 1, 5
# Elementos no comunes -> 6, 7, 2, 4

print(function(array1, array2, True))
print(function(array1, array2, False))