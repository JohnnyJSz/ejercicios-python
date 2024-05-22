""" 
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente. 
"""

text = 'hola mundo cruel'

def capitalise_first_leter(text: str):
  # Lista para almacenar las palabras resultado
  final_list_of_words = list()

  # Separadas las palabras por espacio y almacenadas en una lista para iterar y trabajar sobre cada una
  list_of_words = text.split(' ')
  for word in list_of_words:
    # Primera letra mayuscula
    first_letter = word[0].upper()
    # El resto de la palabra
    rest_of_word = word[1:]
    # Palabra añadida a la lista final
    final_list_of_words.append(first_letter + rest_of_word)

  # Concatenar las palabras de la lista final usando espacio
  result = ' '.join(final_list_of_words)
  # Devuelve la palabra resultado
  return result

result = capitalise_first_leter(text)
print(result)