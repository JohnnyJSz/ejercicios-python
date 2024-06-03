""" 
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
- EXTRA: ¿Eres capaz de dibujar más figuras?
"""

def print_square_or_triangle(height, polygon):
  count = height
  if polygon.lower() == 'cuadrado':
    while count > 0:
      print(' * ' * height)
      count -= 1
  elif polygon.lower() == 'triangulo':
    triangle_height = 1
    while count > 0:
      print(' * ' * triangle_height)
      count -= 1
      triangle_height += 1
  else:
    print('not supported polygon, try square, triangle or pentagon')

print('Square')
print_square_or_triangle(6, 'Cuadrado')
print('Triangle')
print_square_or_triangle(4, 'TRIANGULO')