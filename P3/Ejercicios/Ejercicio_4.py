# EJERCICIO 4 - FILTADO DE IMAGENES

# 4.1. Tome una imagen cualquiera e implemente el código anterior para aplicar un 
# filtrado. Muestre en una ventana la imagen original y la resultante.
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

# Load the image
src = np.array(Image.open('building4.jpg'))

# Define the emboss filter kernel
H = np.array([
    [0, -1, -1],
    [1, 0, -1],
    [1, 1, 0]
])

# Apply the emboss filter
dst = cv2.filter2D(src, -1, H)

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image
ax[0].imshow(src)
ax[0].set_title('Original Image')

# Display the filtered image
ax[1].imshow(dst)
ax[1].set_title('Emboss Filter')

# Show the plot
plt.show()
"""
# 4.2. Repita lo anterior para los distintos tipos de filtros indicados en la tabla 2.
"""
# ---------------------
# - Realce 2 (Emboss) -
# ---------------------
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

# Load the image
src = np.array(Image.open('building4.jpg'))

# Define the emboss filter kernel
H = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])

# Apply the emboss filter
dst = cv2.filter2D(src, -1, H)

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image
ax[0].imshow(src)
ax[0].set_title('Original Image')

# Display the filtered image
ax[1].imshow(dst)
ax[1].set_title('Emboss 2 Filter')

# Show the plot
plt.show()
"""
# --------------------------
# - Agudizado (Sharpennig) -
# --------------------------
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

# Load the image
src = np.array(Image.open('building4.jpg'))

# Define the emboss filter kernel
H = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply the emboss filter
dst = cv2.filter2D(src, -1, H)

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image
ax[0].imshow(src)
ax[0].set_title('Original Image')

# Display the filtered image
ax[1].imshow(dst)
ax[1].set_title('Sharpening Filter')

# Show the plot
plt.show()
