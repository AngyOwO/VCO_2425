
# EJERCICIO 4 - VISUALIZACIÓN 3D
# ------------------------------

# ------------------------------------------------------------------------------
# 4.1 -> Tome alguna de las imágenes anteriores, de tipo grayscale, y representala
# como una supericie empleando las funciones plt.contourf y numpy.meshgrid

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open image with grayscale
img1 = Image.open('Verduras.tif')

camera = np.array(img1, dtype=np.float32)

# Creating a grid
x = np.linspace(0, camera.shape[1] - 1, camera.shape[1])
y =  np.linspace(0, camera.shape[0] - 1, camera.shape[0])
X, Y = np.meshgrid(x,y)

Z = camera

scale_factor = 0.1
Z_small = Z * scale_factor

# Extract grayscale values from Z_small
Z_gray = np.mean(Z_small, axis=2)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection = '3d')

print("X shape:", X.shape)
print("Y shape:", Y.shape)
print("Z_small shape:", Z_small.shape)

ax.plot_surface(X,Y,Z_gray)

# Contour plot
plt.show()


