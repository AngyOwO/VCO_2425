# EJERCICIO 5 - FILTRADO GAUSSIANO Y DE MEDIANA

# 5.1. Tome una imagen cualquiera e introduzca un ruido Salt&Papper o un ruido 
# Gaussiano. Para esto abra el archivo ‘noise.py’ que se encuentra en PoliformaT 
# y estudie las funciones indicadas.

import cv2
import numpy as np
from noise import saltAndPepper_noise

# Cargar la imagen
img = cv2.imread('building4.jpg')  # Reemplaza con la ruta de tu imagen

# Verificar si la imagen se ha cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Aplicar ruido Salt & Pepper
    percent = 0.05  # Porcentaje de ruido (5%)
    noisy_img = saltAndPepper_noise(img.copy(), percent)  # Usamos .copy() para no modificar la original

    # Mostrar la imagen original y la imagen con ruido
    cv2.imshow('Imagen Original', img)
    cv2.imshow('Imagen con Ruido Salt & Pepper', noisy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 5.2. . Añada un ruido gaussiano y aplique a la imagen con ruido un filtrado Gaussiano
#  con la función anterior. Muestre en una ventana la imagen original y la resultante.

import cv2
import numpy as np
from noise import gaussian_noise
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('building4.jpg')  # Reemplaza con la ruta de tu imagen

# Verificar si la imagen se ha cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Aplicar ruido gaussiano
    noisy_img = gaussian_noise(img.copy())  # Usamos .copy() para no modificar la original

    # Aplicar filtrado Gaussiano
    filtered_img = cv2.GaussianBlur(noisy_img, (5, 5), 0)

    # Convertir las imágenes de BGR a RGB para mostrarlas correctamente
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    noisy_img_rgb = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2RGB)
    filtered_img_rgb = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)

    # Mostrar las imágenes en una única ventana
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Imagen Original')
    plt.axis('off')  # Ocultar los ejes

    plt.subplot(1, 3, 2)
    plt.imshow(noisy_img_rgb)
    plt.title('Imagen con Ruido Gaussiano')
    plt.axis('off')  # Ocultar los ejes

    plt.subplot(1, 3, 3)
    plt.imshow(filtered_img_rgb)
    plt.title('Imagen Filtrada')
    plt.axis('off')  # Ocultar los ejes

    plt.tight_layout()  # Ajustar el espacio entre las subgráficas
    plt.show()  # Mostrar la ventana con las imágenes

# 5.3. Repita lo anterior para el filtro de mediana y compare los resultados.

import cv2
import numpy as np
from noise import gaussian_noise
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('building4.jpg')  # Reemplaza con la ruta de tu imagen

# Verificar si la imagen se ha cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Aplicar ruido gaussiano
    noisy_img = gaussian_noise(img.copy())  # Usamos .copy() para no modificar la original

    # Aplicar filtrado de mediana
    filtered_img_median = cv2.medianBlur(noisy_img, 5)

    # Convertir las imágenes de BGR a RGB para mostrarlas correctamente
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    noisy_img_rgb = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2RGB)
    filtered_img_median_rgb = cv2.cvtColor(filtered_img_median, cv2.COLOR_BGR2RGB)

    # Mostrar las imágenes en una única ventana
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Imagen Original')
    plt.axis('off')  # Ocultar los ejes

    plt.subplot(1, 3, 2)
    plt.imshow(noisy_img_rgb)
    plt.title('Imagen con Ruido Gaussiano')
    plt.axis('off')  # Ocultar los ejes

    plt.subplot(1, 3, 3)
    plt.imshow(filtered_img_median_rgb)
    plt.title('Imagen Filtrada con Mediana')
    plt.axis('off')  # Ocultar los ejes

    plt.tight_layout()  # Ajustar el espacio entre las subgráficas
    plt.show()  # Mostrar la ventana con las imágenes