# EJERCICIO 3 - TRANSFORMACIONES DE PUNTOS
# ----------------------------------------

# 3.1. Escriba el script anterior en un archivo “RotacionPuntos.py”
"""
import matplotlib.pyplot as plt
import numpy as np
import string
import math

# Defining points
a, b, c, d = (0, 1, 1), (1, 0, 1), (0, -1, 1), (-1, 0, 1) # points a, b, c y d en coordenadas homogéneas
A = np.array([a, b, c, d])

# Transformation matrix
T_s = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])     # scaling by 2x
T_r = np.array ([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])   # rotation by 90 degrees
T = T_s @ T_r

# 3x3 Identity transformation matrix
I = np.eye(3)
color_lut = 'rgbc'

# Setting up the visualization
fig = plt.figure()
ax = plt.gca()
xs_s = []
ys_s = []
i=0

# Transforming and visualizing points
for row in A:
   output_row = T @ row # transforming points
   x, y, h = row
   x_s, y_s, k = output_row
   xs_s.append(x_s)
   ys_s.append(y_s)
   c = color_lut[i]
   plt.scatter(x, y, color=c)
   plt.scatter(x_s, y_s, color=c)
   plt.text(x + 0.15, y, f"{string.ascii_letters[int(i)]}")
   plt.text(x_s + 0.15, y_s, f"{string.ascii_letters[int(i)]}'")
   i+=1

# Connecting points and configuring axes
xs_s.append(xs_s[0])
ys_s.append(ys_s[0])
plt.plot(x_s, y_s, color="gray", linestyle='dotted')
plt.plot(xs_s, ys_s, color="gray", linestyle='dotted')
ax.set_xticks(np.arange(-10, 10, 1.0))
ax.set_yticks(np.arange(-10, 10, 1.0))
plt.grid()
plt.show() 
"""
# 3.2. Cambie la matriz de transformación afín T para que produzca 
# una traslación simple t=(tx, ty)=(-3, 3).Cree una segunda matriz 
# de transformación R para una rotación de ángulo Theta=30 grados. 
# Aplique las transformaciones indicadas a los puntos y muestre 
# los resultados

import matplotlib.pyplot as plt
import numpy as np
import string
import math

# Definition of points 
a, b, c, d = (0, 1, 1), (1, 0, 1), (0, -1, 1), (-1, 0, 1) # points a, b, c y d en coordenadas homogéneas
A = np.array([a, b, c, d])

# Transformation matrix
T = np.array([[1, 0, -3], [0, 1, 3], [0, 0, 1]]) # Translation matrix
theta = 30 * math.pi / 180  # Convert degrees to radians for rotation
R = np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]) # rotación
TR = T @ R # Combine translation and rotation

# Setup for visualization
fig = plt.figure()
ax = plt.gca()
xs_s = []
ys_s = []
i=0
color_lut = 'rgbc'

# Transformation and visualization of points
for row in A:
   output_row = T @ row # Transform the points using the translation matrix
   x, y, h = row
   x_s, y_s, k = output_row
   xs_s.append(x_s)
   ys_s.append(y_s)
   c = color_lut[i]
   plt.scatter(x, y, color=c)
   plt.scatter(x_s, y_s, color=c)
   plt.text(x + 0.15, y, f"{string.ascii_letters[int(i)]}")
   plt.text(x_s + 0.15, y_s, f"{string.ascii_letters[int(i)]}'")
   i+=1

# Connect points and configure axes
xs_s.append(xs_s[0])
ys_s.append(ys_s[0])
plt.plot(x_s, y_s, color="gray", linestyle='dotted')
plt.plot(xs_s, ys_s, color="gray", linestyle='dotted')
ax.set_xticks(np.arange(-10, 10, 1.0))
ax.set_yticks(np.arange(-10, 10, 1.0))
plt.grid()
plt.show()