
# EJERCICIO 3 - ARITMÉTICA CON IMÁGENES
# -------------------------------------

# ------------------------------------------------------------------------------
# 3.1 -> Lea las imágenes 'cameraman.tif' y 'moon.tif', que se encuentran 
# en la instalación de MATLAB. 

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Open the TIFF images files
img1 = Image.open('Verduras.tif')
img2 = Image.open('Fruta.tif')

# Create a image composed with the right rize
composite_img = Image.new('RGB', (img1.width + img2.width, 
                                  max(img1.height, img2.height)))

# Pegar las imágenes individuales en la imagen compuesta
composite_img.paste(img1, (0, 0))
composite_img.paste(img2, (img1.width, 0))

# Mostrar la imagen compuesta
composite_img.show()

# ------------------------------------------------------------------------------
# 3.2 -> Redimensiónalas para que tengan el mismo tamaño.

from PIL import Image

with Image.open('Verduras.tif') as img1:
    new_size = (256, 256)
    img1_new =  img1.resize(new_size)
    img1_new.save('Verduras_256_256.tif')

with Image.open('Fruta.tif') as img2:
    new_size = (256, 256)
    img2_new =  img2.resize(new_size)
    img2_new.save('Fruta_256_256.tif')

# Show the images
img1_new.show()
img2_new.show()

# ------------------------------------------------------------------------------
# 3.3 -> Realice algunas operaciones aritméticas entre ellas y visualice el 
# resultado.

from PIL import Image, ImageChops

# Open images 
with Image.open('Verduras.tif') as img1:
    with Image.open('Fruta.tif') as img2:

        # Add images
        img_sum = ImageChops.add(img1, img2)
        img_sum.save('Suma_Verdura_y_Fruta.tif')

        # Subtract images
        img_diff = ImageChops.difference(img1, img2)
        img_diff.save('Diferencia_Verdura_y_Fruta.tif')

        # Multiply images
        img_product = ImageChops.multiply(img1, img2)
        img_product.save('Producto_Verdura_y_Fruta.tif')

# Show the results
img_sum.show()
img_diff.show()
img_product.show()

#  ------------------------------------------------------------------------------
# 3.4 -> Realice la combinación lineal siguiente y visualice:
# [ S = IMG1 * 1.8 - IMG2 * 1.2 + 128 ]

from PIL import Image
import numpy as np

# Open images
with Image.open('Verduras.tif') as img1:
    new_size = (500, 500)
    img1 =  img1.resize(new_size)
    img1.save('Verduras_500_500.tif')

with Image.open('Fruta.tif') as img2:
    new_size = (500, 500)
    img2 =  img2.resize(new_size)
    img2.save('Fruta_500_500.tif')

# Convert images to arrangements numpy
img1_array = np.array(img1)
img2_array = np.array(img2)

# Multiply the images by the corresponding factors
img1_array_multiplied = img1_array * 1.8
img2_array_multiplied = img2_array * 1.2

# Subtract the image resulting from the multiplication of IMG2 from the image resulting from the multiplication of IMG1
img_resulting_array = img1_array_multiplied - img2_array_multiplied

# Add 128 to the resulting image
img_resulting_array += 128

# Make sure the values ​​fit into the correct range
img_resulting_array = np.clip(img_resulting_array, 0, 255)

# Convert numpy array back to an image
img_resulting = Image.fromarray(img_resulting_array.astype(np.uint8))

# Show the resulting image
img_resulting.show()










