""" 
Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
  o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan
  automáticamente. 
"""

def order_matrix(my_list, order):
  # tiramos un error si se introduce mal el valor 'order'
  if order.lower() not in ["asc", "desc"]:
    raise ValueError("¡El orden debe ser 'Asc' o 'Desc'!")

  ordered_list = []

  while my_list:
    if order.lower() == "asc":
      value = min(my_list)
    else:
      value = max(my_list)

    ordered_list.append(value)
    # elimina el numero minimo/maximo de la lista original para no comprobarlo en la siguiente iteracion
    my_list.remove(value)

  return ordered_list

print(order_matrix([1,4,6,2,7,3], 'asc')) #[1, 2, 3, 4, 6, 7]
print(order_matrix([1,4,6,2,7,3], 'desc')) #[7, 6, 4, 3, 2, 1]