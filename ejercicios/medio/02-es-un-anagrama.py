""" Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama. """

# Ejemplos de anagramas:
# españa - apañes - False
# enrique - quieren - True
# ballena - llenaba - False
# saco - cosa - True
# teta - feta - False -> la f no esta en la otra palabra
# teta - etat - True -> reorganizando las letras conseguimos la otra palabra
# teta - teta - False -> las palabras son iguales

def is_anagram(first_word, second_word):
  # crea listas con cada palabra para comprobar que las letras se reorganizan TODAS
  list_first_word = list(first_word)
  list_second_word = list(second_word)

  # define condiciones
  are_same_words = first_word == second_word
  are_same_len = len(first_word) == len(second_word)
  
  # comprubea que dos palabras exactamente iguales no son anagrama.
  if are_same_words:
    return {'result': False, 'reason': 'Same words, examples are not valid.'}

  if not(are_same_words) and not(are_same_len):
      return {'result': False, 'reason': 'Different words of different length'}

  if not(are_same_words) and are_same_len:
    for i in range(len(first_word)):
      # comprueba que reordena TODAS las letras, es decir, que una letra no se encuentra en el mismo indice en ambas listas.
      if list_second_word[i] == list_first_word[i]:
        # return False
        return {'result': False, 'reason': 'Different words of the same length where some letters in the second word occupies the same position as it does in the first word.'}

  # return True
  return {'result': True, 'reason': 'Different words of the same length where no letter in the second word occupies the same position as it does in the first word.'}

first_word = input('Primera palabra:')
second_word = input('Segunda palabra:')
result = is_anagram(first_word, second_word)
print(f'is anagram? {result['result']}\nReason: {result['reason']}')