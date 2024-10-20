# EJERCICIO 2 - COMBINACIÓN DE TRANSFORMACIONES DE LA IMAGEN
# ----------------------------------------------------------

# 2.1. Utilice el script “checkerboard.py” para crear una imagen 
# de un tablero de ajedrez (Checkerboard) de 10x10 cuadrados de 
# 20 pixeles de lado. Muéstrela en una imagen.

# Python program to print nXn
# checkerboard pattern using numpy
"""
import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# function to return a Checkerboard graylevel image of n x n squares each of size 'sz'
def checkboard(grid= 10, square_size = 10):
     
    print("Checkerboard pattern:")
 
    # create a n * n matrix
    x = np.zeros((grid, grid), dtype = np.uint8)
 
    # fill with 255 the alternate rows and columns
    x[1::2, ::2] = 255
    x[::2, 1::2] = 255
    
    sz = grid * square_size 
    size = (sz,sz)
    img = Image.fromarray(x, mode='L')
    img_res = img.resize(size, resample=Image.Resampling.NEAREST)
    return img_res

# Main code
img =checkboard(10,20)   
plt.figure(figsize=(9,5))

plt.imshow(img, cmap='gray')  # Mostrar la imagen en escala de grises
plt.axis('off')  # Ocultar los ejes
plt.show()

img.save('checkerboard.jpg')
"""
# 2.2. Cree una matriz de transformación afín T para una traslación simple t=(tx,ty)=(100,50). 
# Cree una segunda matriz de transformación R para una rotación de ángulo Theta=30 grados. 
# Aplique las transformaciones indicadas a la imagen y muestre los resultados.

# Python program to print nXn
# checkerboard pattern using numpy
 
import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image
import math

# function to return a Checkerboard graylevel image of n x n squares each of size 'sz'
def checkboard(grid= 10, square_size = 10):
     
    print("Checkerboard pattern:")
 
    # create a n * n matrix
    x = np.zeros((grid, grid), dtype = np.uint8)
 
    # fill with 255 the alternate rows and columns
    x[1::2, ::2] = 255
    x[::2, 1::2] = 255
    
    # Size of the image
    sz = grid * square_size 
    size = (sz,sz)
    img = Image.fromarray(x, mode='L')
    img_res = img.resize(size, resample=Image.Resampling.NEAREST)
    return img_res

# Create the checkerboard image
img =checkboard(10,20)   # Create a checkerboard with 10x10 squares of 20x20 pixels

# Transformation parameters
tx = 100  # Translation offset in the x direction
ty = 50   # Translation offset in the y direction

# Create an affine transformation matrix for translation
T = (1, 0, tx, 0, 1, ty, 0, 0, 1)

# Apply affine transformation (translation)
img_translated = img.transform((img.width, img.height), Image.AFFINE, T, resample=Image.BICUBIC)

# Parameters for rotation
theta = 30 * math.pi / 180  # Convertir ángulo a radianes

# Create an affine transformation matrix for rotation
R = (math.cos(theta), -math.sin(theta), 0,
     math.sin(theta), math.cos(theta), 0,
     0, 0, 1)

# Apply affine transformation (rotation)
img_rotated = img_translated.transform((img.width, img.height), Image.AFFINE, R, resample=Image.BICUBIC)

# Display original, translated, and rotated images
plt.figure(figsize=(15, 6))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Imagen original')

plt.subplot(132)
plt.imshow(np.asarray(img_translated), cmap='gray')
plt.title('Imagen traducida')

plt.subplot(133)
plt.imshow(np.asarray(img_rotated), cmap='gray')
plt.title('Imagen rotada')

plt.show() # Show all the plots

# Save the rotated image
img_rotated.save('checkerboard_transformed.jpg')
