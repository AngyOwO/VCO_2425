# EJERCICIO 6 - DETECCIÓN DE BORDES

# 6.1. Tome una imagen cualquiera y pruebe las funciones de Sobel para detección
# de bordes horizontales y verticales.

import cv2
import numpy as np

img = cv2.imread('building4.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=3)

cv2.imshow('Bordes horizontales', grad_x)
cv2.imshow('Bordes verticales', grad_y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6.2 y 6.3. Combine el Laplaciano y el Gaussiano para crear un LoG y muestre 
# los distintos resultados en ventanas diferentes.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('building4.jpg')
# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano
sigma = 1.0  # Desviación estándar del filtro Gaussiano
gaussian_blur = cv2.GaussianBlur(gray, (5, 5), sigma)

# Aplicar el operador Laplaciano
laplacian = cv2.Laplacian(gaussian_blur, cv2.CV_64F)

# Convertir a tipo de datos de 8 bits
laplacian = cv2.convertScaleAbs(laplacian)

# Mostrar la imagen original y el resultado del LoG
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Resultado de LoG')
plt.imshow(laplacian, cmap='gray')
plt.axis('off')

plt.show()
