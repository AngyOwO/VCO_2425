# EJERCICIO 4 - VISUALIZACIÓN DE OPENCV EMPLEANDO MATPLOTLIB
# ----------------------------------------------------------

# 4.1. Cree un archivo “VisualizaOpenCV.py” y escriba el script anterior, 
# añadiendo las instrucciones indicadas. Compruebe si se visualizan bien las 
# imágenes con Matplotlib. ¿Qué problema se plantea?

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading and resizing an image
src = cv2.imread('Verduras.png')
dst = cv2.resize(src, (256, 256), interpolation=cv2.INTER_CUBIC)

# Displaying images
cv2.imshow('Imagen original', src)
cv2.imshow('Imagen escalada', dst)

# Save images
cv2.imwrite('imagen_original.png', src)
cv2.imwrite('imagen_escalada.png', dst)
"""
# Matplotlib
plt.subplot(121),plt.imshow(src),plt.title('Input')     # Visualización en matpolotlib.pyplot
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
"""
# Waiting for a key press and closing windows
cv2.waitKey(0)
cv2.destroyAllWindows()