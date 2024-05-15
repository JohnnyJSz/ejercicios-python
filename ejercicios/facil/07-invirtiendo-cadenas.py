""" 
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
text = 'Hola mundo'

def invertir_string(string):
  l1 = list(string)
  l2 = list(string)
  
  for index, el in enumerate(l1):
    index += 1
    l2[-index] = el

  result = ''.join(l2)
  return result;

result = invertir_string(text)
print(f'El resultado de invertir la cadena de texto {text} es:',result)