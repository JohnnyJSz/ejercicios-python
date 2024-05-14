""" 
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo:
  https://images.unsplash.com/photo-1715090156594-aaa3ed5900b9?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px. 
"""

# biblioteca más popular para trabajar con imágenes en Python -> PIL (Pillow).
from PIL import Image
# Se utiliza la biblioteca requests para descargar la imagen desde la URL.
import requests
# BytesIO se usa para tratar el contenido descargado como un archivo en memoria.
from io import BytesIO

# imagen url
# image_url = 'https://images.unsplash.com/photo-1715090156594-aaa3ed5900b9?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' # 2071 x 1380
image_url = 'https://cdn2.meadd.com/photos/full/73102237.jpg' # 150 x 150

# descargar la imagen
response = requests.get(image_url)

image_bytes = BytesIO(response.content)

# abrir la imagen
# Image.open() de Pillow abre la imagen desde el objeto BytesIO.
my_image = Image.open(image_bytes)

# obtener los valores de ancho y alto de la imagen
ancho, alto = my_image.size

# calcular el aspect ratio.
# simplificar la proporcion de los valores de ancho y alto
# 1- Obtener alto y ancho
# 2- Encontrar el MCD (Maximo Comun Divisor)
# 3- Dividir ambos numeros (ancho y alto) por el MCD para obtener la relacion simplificada.

# Encontar el MCD (algoritmo de Euclides)
# 1- Dividir el numero mayor por el menor y obtener el residuo
# 2- Reemplazar el numero mayor por el menor y el menor por el residuo.
# 3- Repetir el proceso hasta que el residuo sea cero. El ultimo numero no cero es el MCD

def mcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

resultado_mcd = mcd(ancho, alto)

# Calcular el aspect ratio
ratio_ancho = ancho // resultado_mcd
ratio_alto = alto // resultado_mcd

print(f'El aspect ratio de la imagen de ancho {ancho}px y alto {alto}px es {ratio_ancho}:{ratio_alto}')
