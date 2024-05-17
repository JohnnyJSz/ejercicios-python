""" 
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente. 
"""
# modulo estandar para trabajar con expresiones regulares
import re

def count_words(text: str):
  # expresion regular para buscar cualquier signo de puntuacion
  # cualquier caracter que no sea una letra, un numero o espacio en blanco
  regex = r'[^\w\s]'
  # convertir el texto a minusculas
  text = text.lower()

  # Separar las palabras por espacio.
  # obtendremos una lista con cada palabra, incluidas palabras con signos de puntuacion.
  list_words = text.split(' ')
  # Creo un dictionario donde almacenar cada palabra con el numero de ocurrencias.
  result_words_dict = dict()

  # Iteramos sobre la lista de palabras
  for each_word in list_words:
    # formateamos cada palabra en la lista para quitar simbolos de puntuacion usando regex
    formatted_word = re.sub(regex, '', each_word)

    # por cada palabra, si la palabra formateada esta en el diccionario, aumentamos en 1 su ocurrencia
    if formatted_word in result_words_dict:
      result_words_dict[formatted_word] += 1
    else: # si no esta, la añadimos al diccionario y asignamos el valor 1 a su ocurrencia
      result_words_dict[formatted_word] = 1

  # iteramos sobre el diccionario usando .items() para poder usar el key (palabra) y el value (num de ocurrencia)
  for key, value in result_words_dict.items():
    # hacemos un print mostrando un mensaje con cada palabra y el num de veces que aparece.
    print(f'La palabra [{key}] se ha repetido [{value}] {'vez' if value == 1 else 'veces'}')


text = 'el perro de pedro es un buen perro, tan buen perro que lo ha llamado Perro y siempre que lo llama grita ¡PERRO!'
count_words(text)