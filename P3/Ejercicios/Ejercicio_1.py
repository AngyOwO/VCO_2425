# EJERCICIO 1 - HISTOGRAMAS

# 1.1 Y 1.2. Tome unas imágenes en color cualesquiera de las utilizadas en las prácticas anteriores, 
# o de las disponibles en PoliformaT. Escriba el código anterior y pruebe el resultado.
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('building4.jpg'))
hr, edges_r = np.histogram(img[:,:,0],256)

fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal
axs[1].stairs(hr, edges_r, label='Red histogram', ec='r')
axs[1].set_title("Step Histograms")
axs[1].legend()

plt.sca(axs[0]) # Para poner en el subplot izquierdo la imagen
plt.imshow(img)
plt.show()
"""
# 1.3. Añada las instrucciones necesarias para obtener el histograma de cada uno de los tres canales
# de color de la imagen RGB – hr, hg, hb - y mostrarlos sobre la misma gráfica.
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('building4.jpg'))

# Separa los canales de color
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

# Calcula el histograma de cada canal
hr, edges_r = np.histogram(r,256)
hg, edges_g = np.histogram(g,256)
hb, edges_b = np.histogram(b,256)

fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal

axs[1].stairs(hr, edges_r, label='Red histogram', ec='r')
axs[1].stairs(hg, edges_g, label='Green histogram', ec='g')
axs[1].stairs(hb, edges_b, label='Blue histogram', ec='b')
axs[1].set_title("Step Histograms")
axs[1].legend()

plt.sca(axs[0]) # Para poner en el subplot izquierdo la imagen
plt.imshow(img)
plt.show()
"""
# 1.4. Modifique alguna de las propiedades de los histogramas, como por ejemplo el número de bins a
#  valor 16 o la ‘density = True, y observe el resultado.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('building4.jpg'))

# Separa los canales de color
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

# Calcula el histograma de cada canal
hr, edges_r = np.histogram(r, bins=16, density=True)
hg, edges_g = np.histogram(g, bins=16, density=True)
hb, edges_b = np.histogram(b, bins=16, density=True)

fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal

axs[1].stairs(hr, edges_r, label='Red histogram', ec='r')
axs[1].stairs(hg, edges_g, label='Green histogram', ec='g')
axs[1].stairs(hb, edges_b, label='Blue histogram', ec='b')
axs[1].set_title("Step Histograms")
axs[1].legend()

plt.sca(axs[0]) # Para poner en el subplot izquierdo la imagen
plt.imshow(img)
plt.show()