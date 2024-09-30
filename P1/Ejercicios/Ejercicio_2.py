
# EJERCICIO 2 - MANIPULACIÓN DE LA IMAGEN
# ---------------------------------------

# ------------------------------------------------------------------------------
# 2.1 -> Utilizando cualquiera de las imágenes introducidas en el ejercicio 
# anterior, aplique distintas transformaciones y compruebe el resultado.

from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Upload the image
img = Image.open('Galaxia.jpg')

# Show the original image
img.show()

# Rotate 45 degrees the image
img = img.rotate(angle = 45,  expand = 1)

# Enlarge the image
img = img.reduce(3)

# Transpose the image
img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

# Show the image
img.show()

# ------------------------------------------------------------------------------
# 2.2 -> Convierta cualquier imagen en color en una imagen de niveles gris y 
# visualice ambas.

from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage import io

# Upload the image
img = Image.open('Galaxia.png')

# Show the original image
img.show()

# Convert the image to grayscale
img_gray = img.convert('L')

# Show the grayscale image
img_gray.show()

# ------------------------------------------------------------------------------
# 2.3 -> Tomar una imagen RGB y muestre los tres componentes R (rojo), G (verde)
# y B (azul) como imagenes de gris separado.

from  PIL import Image
import numpy as np

# Upload the image
img = Image.open('Verduras.png')

# Convert the image to R
img_red = img.getchannel('R')

# Show the red channel image
img_red.show()

# Convert the image to G
img_green = img.getchannel('G')

# Show the green channel image
img_green.show()

# Convert the image to B
img_blue = img.getchannel('B')

# Show the blue channel image
img_blue.show()









