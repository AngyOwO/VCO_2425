# EJERCICIO 3 - AJUSTE DE CONTRASTE DE UNA IMAGEN

# 3.1. Tome una imagen cualquiera e implemente un programa para ajustar el contraste
# mediante la función que se muestra en la figura 3. Utilice min=100 máx.=200, o 
# cualesquiera de valores que desee. Muestre en una ventana la imagen original y la 
# resultante.
"""
import cv2
import numpy as np

# Load the image
img = cv2.imread('building4.jpg')

# Define the contrast adjustment function
def imadjust(img, low_in, high_in):
    min_val = low_in
    max_val = high_in
    img_out = np.round(255.0 * (img - min_val) / (max_val - min_val + 1)).astype(np.uint8)
    img_out[img < min_val] = 0
    img_out[img > max_val] = 255
    return img_out

# Adjust the contrast with low_in=100 and high_in=200
low_in = 100
high_in = 200
img_contrast = imadjust(img, low_in, high_in)

# Display the original and resulting images
cv2.imshow('Original', img)
cv2.imshow('Contrast Adjusted', img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# 3.2. Repita lo anterior, pero con las LUT indicadas en la figura 7.

import cv2
import numpy as np

# Load the image
img = cv2.imread('building4.jpg')

# Define the contrast adjustment function using LUT
def imadjust(img, min_val, max_val):
    LUT = np.zeros(256, dtype=np.uint8)
    LUT[max_val+1:] = 255
    LUT[min_val:max_val+1] = np.linspace(start=0, stop=255, num=(max_val-min_val)+1, endpoint=True, dtype=np.uint8)
    img_out = LUT[img]
    return img_out

# Adjust the contrast with min_val=100 and max_val=200
min_val = 100
max_val = 200
img_contrast = imadjust(img, min_val, max_val)

# Display the original and resulting images
cv2.imshow('Original', img)
cv2.imshow('Contrast Adjusted', img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
