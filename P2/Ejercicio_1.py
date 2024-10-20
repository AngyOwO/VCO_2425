# EJERCICIO 1 - TRANSFORMACIONES SIMPLES DE LA IMAGEN
# ---------------------------------------------------
# 1.1. Tome una imagen cualquiera de las utilizadas en la práctica anterior, o de las 
# disponibles en PoliformaT. Muestre la imagen en una ventana empleando el script 
# “Afin_image.py”.

import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# Open an image
img = Image.open('Verduras.png')

# Get the transformed image
img_t = img
plt.figure(figsize=(10, 6)) # Create a new figure with a specified size
plt.subplot(121)
plt.imshow(img) # Display the original image
plt.title('Original Image')
plt.subplot(122)

# Display the transformed image as a numpy array
plt.imshow(np.asarray(img_t))
plt.title('Transformed Image')

plt.show()  # Show the figure with both subplots

# 1.2. Modifique el script anterior para aplicar una rotación de +10º a la imagen, 
# siguiendo el ejemplo anterior, y muestre el resultado en la otra ventana, o 
# utilice la misma ventana empleando la función matplotlib.subplot. 

import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# Open an image
img = Image.open('Verduras.png')

# Rotate the image by +10 degrees
img_rotated = img.rotate(10)

# Prepare to display the original and transformed image
plt.figure(figsize=(10, 6)) # Create a figure with a specified size

# Create the first subplot for the original image
plt.subplot(121)
plt.imshow(img)
plt.title('Imagen original')

# Create the second subplot for the rotated image
plt.subplot(122)
plt.imshow(np.asarray(img_rotated))
plt.title('Imagen rotada')

# Show the plots
plt.show()  

# 1.3. Cambien la matriz T para introducir un desplazamiento y un escalado. 
# Varíe esos parámetros y compruebe el resultado.

import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# Open an image
img = Image.open('Verduras.png')

# Define transformation parameters
desplazamiento_x = 50
desplazamiento_y = 30
escalado_x = 0.8
escalado_y = 0.8

# Rotate the image by 10 degrees
img_rotated = img.rotate(10)

# Apply an affine transformation (displacement and scaling)
img_transformed = img_rotated.transform((img.width, img.height), 
                                         Image.AFFINE, 
                                         (escalado_x, 0, desplazamiento_x, 
                                          0, escalado_y, desplazamiento_y, 
                                          0, 0, 1), 
                                         resample=Image.BICUBIC)

# Display the original image, the rotated image, and the transformed image
plt.figure(figsize=(15, 6))

# Create a subplot for the original image
plt.subplot(131)
plt.imshow(img)
plt.title('Imagen original')

# Create a subplot for the rotated image
plt.subplot(132)
plt.imshow(np.asarray(img_rotated))
plt.title('Imagen rotada')

# Create a subplot for the transformed image
plt.subplot(133)
plt.imshow(np.asarray(img_transformed))
plt.title('Imagen transformada')

# Display the plot
plt.show()
