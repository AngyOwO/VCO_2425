
# EJERCICIO 1 - TRABAJAR CON IMÁGENES
# -----------------------------------

# ------------------------------------------------------------------------------
# 1.1 -> Descarga una imagen, pon los archivos en la carpeta actual
# y muestrela en una ventana

from PIL import Image

# Open the PNG image file
img = Image.open('Galaxia.png')

# Show the image
img.show()

# ------------------------------------------------------------------------------
# 1.2 -> Lea alguno de los archivos de color de tipo tif mostrandolo
# en una ventana mediante Pillow. Si no se vusializa bien intente poner el mapa
# de colores o paleta que se corresponda. Muestre también la barra de colores al
# lado de la imagen. ¿Cuántos colores tiene?

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Open the TIFF image file
img = Image.open('galaxia2.tif')

# Convert the image to a numpy array
img_array = np.array(img)
imgplot = plt.imshow(img)
plt.colorbar()

# Show the image
plt.show()

# ------------------------------------------------------------------------------
# 1.3 -> Reduzca el número de colores de la imagen anterior a 16 y
# múestrela. Compare ambas imágenes visualmente.

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import img_as_ubyte

# Open the TIFF image file
img = Image.open('galaxia2.tif')

# Use the quantize method to reduce the number of colors in the image to 16.
img2 = img.quantize(colors = 16)

# Convert both images to numpy arrays using np.asarray, and display both images.
img_array =  np.asarray(img)
imgplot = plt.imshow(img_array)
img2_array = np.asarray(img2)
imgplot2 = plt.imshow(img2_array)

# Add a colorbar to the plot
plt.colorbar()

# Show the image
plt.show()

# ------------------------------------------------------------------------------
# 1.4 -> Repita las operaciones anteriores con una imagen de tipo jpg. 
# Conviértela primero a tipo 'P' con paleta y repita las operaciones anteriores.

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import img_as_ubyte

# Open the TIFF image file
img = Image.open('Galaxia.jpg')

# Convert the image to 'P' mode
img = img.convert(mode= 'P')

# Convert the image to numpy array and display it
img_array =  np.asarray(img)
imgplot = plt.imshow(img_array)
# Add a colorbar
plt.colorbar()
plt.show()

# Use the quantize method to reduce the number of colors in the image to 16.
img2 = img.quantize(colors = 16)

# Convert the image to numpy array and display it.
img2_array = np.asarray(img2)
imgplot2 = plt.imshow(img2_array)

# Add a colorbar
plt.colorbar()

# Show the image
plt.show()
