# EJERCICIO 5 - COMBINACIÓN DE TRANSFORMACIONES SIMPLES EN OPENCV
# ---------------------------------------------------------------

# 5.1. Repita el ejercicio 1, de concatenación de transformaciones simples de
#  la imagen, pero utilizando las funciones de OpenCV antes indicadas. Para 
# esto cree el script “warpAffineOpenCV.py”

import cv2
import numpy as np

# Load the image
img = cv2.imread('Verduras.png')

# Define transformation parameters
desplazamiento_x = 50
desplazamiento_y = 30
escalado_x = 0.8
escalado_y = 0.8

# Apply rotation of +10 degrees to the image
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 10, 1.0)
img_rotated = cv2.warpAffine(img, M, (w, h))

# Apply affine transformation (scaling and translation)
M = np.float32([[escalado_x, 0, desplazamiento_x],
                [0, escalado_y, desplazamiento_y]])
img_transformed = cv2.warpAffine(img_rotated, M, (w, h))

# Display the original image, the rotated image, and the transformed image
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen rotada', img_rotated)
cv2.imshow('Imagen transformada', img_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
