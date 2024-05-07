""" 
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo. 
"""
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
def area_of_a_polygon(polygon):
  type, base, height = polygon['type'], polygon['base'], polygon['height']

  area_triangle = (base * height)/2
  area_square = base * height 
  area_rectangle = base * height

  # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  switcher = {
    'triangle': area_triangle,
    'square': area_square,
    'rectangle': area_rectangle
  }

  # - Imprime el cálculo del área de un polígono de cada tipo.
  print(f'The area of {type} is {switcher[type]} sqr units.')

# - La función recibirá por parámetro sólo UN polígono a la vez.
area_of_a_polygon({'type': 'triangle', 'base': 6, 'height': 4})
area_of_a_polygon({'type': 'square', 'base': 5, 'height': 5})
area_of_a_polygon({'type': 'rectangle', 'base': 6, 'height': 10})

# ----

class Polygon:
  """ Base class for Polygon objects """
  def __init__(self, base, height) -> None:
    """ 
    Initial parameters
    param base: base length
    param height: height length 
    """
    if base <= 0 or height <= 0:
      raise ValueError('Base and Height must be greater than 0')
    self.base = base
    self.height = height

  def print_area(self):
    # self.__class__.__name__: expression used to obtain the name of the class to which a particular instance belongs

    # Polymorphism - It allows that a sub class provides its own implementation for area() method
    # Python search for area() method inside the class self.__class__ (for example, Square)
    # if it finds area(), then it call the method from there.
    # if it doesnt find area() method in Square, then Python backtracks through the class hierarchy until it finds an implementation.
    # This process continues until reach the base class Polygon, where finally it will rais an exception if there is not an implementation available.
    print(f'The area of polygon {self.__class__.__name__} is {self.area()} sqr units.')

# Inheritance - Triangle inherits from Polygon
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
class Triangle(Polygon):
  def area(self):
    return (self.base * self.height) / 2

# Inheritance - Square inherits from Polygon
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
class Square(Polygon):
  # Square will only accept one param, as all of its sides are the same
  # Square constructor with one param
  def __init__(self, side) -> None:
    # call the constructor of Polygon and use side as base and height
    super().__init__(side, side)
    
  def area(self):
    # this method calculates the area of a square using self.base as base and height are the same value
    # self.side is not an attribute defined in Square. Square relies on the attributes inherited from Polygon
    return self.base * self.base

# Inheritance - Rectangle inherits from Polygon
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
class Rectangle(Polygon):
  def area(self):
    return self.base * self.height

# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
def area(polygon: Polygon) -> None:
  # - Imprime el cálculo del área de un polígono de cada tipo.
  polygon.print_area()

# - La función recibirá por parámetro sólo UN polígono a la vez.
area(Triangle(6,4))
area(Square(5))
area(Rectangle(6, 10))































# class Triangle(Polygon):
  # def __init__(self, base, height) -> None:
  #   super().__init__(base, height)
  #   self.triangle = 'triangle'
  # def area(self):
  #   return (self.base * self.height) / 2
  # def print_area(self):
  #   print(f'The area of Triangle is {self.area()} sqr units')

# class Square(Polygon):
#   def __init__(self, side) -> None:
#     super().__init__(side, side)

#   def area(self):
#     return self.base * self.base
  
#   def print_area(self):
#     print(f'The area of Square is {self.area()} sqr units')

# class Rectangle(Polygon):
#   def __init__(self, side, height):
#     super().__init__(side, height)

#   def area(self):
#     return self.base * self.height
  
#   def print_area(self):
#     print(f'The area of Rectangle is {self.area()} sqr units')


# triangle = Triangle(6, 4)
# triangle.print_area()

# square = Square(5)
# square.print_area()

# rectangle = Rectangle(5, 8)
# rectangle.print_area()