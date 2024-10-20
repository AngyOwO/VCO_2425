# EJERCICIO 2 - ECUALIZACIÓN DEL HISTOGRAMA

# 2.1. Tome una imagen de niveles de gris, o convierta una de color a gris, y muestre 
# su histograma. Después realice la ecualización del histograma y muestre la imagen 
# resultante y su histograma. Compruebe si, efectivamente, ese histograma resultante 
# es más uniforme.
"""
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('building4.jpg')

# Convertir la imagen a escala de grises
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Realizar la ecualización del histograma
img_equalized = cv2.equalizeHist(img_gray)

# Mostrar la imagen original y la ecualizada
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Mostrar imagen original
axs[0].imshow(img_gray, cmap='gray')
axs[0].set_title('Imagen Original')
axs[0].axis('off')

# Mostrar imagen ecualizada
axs[1].imshow(img_equalized, cmap='gray')
axs[1].set_title('Imagen Ecualizada')
axs[1].axis('off')

plt.show()

# Calcular y mostrar el histograma de la imagen ecualizada
hist_equalized = cv2.calcHist([img_equalized], [0], None, [256], [0, 256])

plt.figure(figsize=(6, 4))
plt.plot(hist_equalized, label='Histograma Ecualizado', color='b')
plt.title('Histograma de la Imagen Ecualizada')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
"""
# 2.2. Pruebe la ecualización con la imagen ‘clahe_1.jpg’ y compruebe si el resultado 
# es satisfactorio. Luego pruebe con CLAHE y compare el resultado con el anterior.

import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('building4.jpg')

# Convertir la imagen a escala de grises
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Crear un objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# Aplicar CLAHE a la imagen en escala de grises
img_equalized = clahe.apply(img_gray)

# Mostrar la imagen original y la ecualizada
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Mostrar imagen original
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title('Imagen Original')
axs[0].axis('off')

# Mostrar imagen ecualizada
axs[1].imshow(cv2.cvtColor(img_equalized, cv2.COLOR_GRAY2RGB))
axs[1].set_title('Imagen Ecualizada con CLAHE')
axs[1].axis('off')

plt.show()

# Calcular y mostrar el histograma de la imagen ecualizada
hist_equalized = cv2.calcHist([img_equalized], [0], None, [256], [0, 256])

plt.figure(figsize=(6, 4))
plt.plot(hist_equalized, label='Histograma Ecualizado con CLAHE', color='b')
plt.title('Histograma de la Imagen Ecualizada con CLAHE')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()