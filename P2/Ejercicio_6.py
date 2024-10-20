import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread('building4.jpg')

# show image
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

# graphic input of 4 points
pts = plt.ginput(4)
print(pts)

# Convert to numpy array
pts = np.array(pts, np.float32)

# Check if we have exactly 4 points
if pts.shape[0] != 4:
    print("Error: Se deben seleccionar exactamente 4 puntos.")
else:
    outs = [[0,0], [200,0], [200,200], [0,200]]
    outs = np.array(outs, np.float32)
    print(outs)

    # Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(pts, outs)

    # Apply the perspective transformation to the image
    transformed_img = cv2.warpPerspective(img, M, (200, 200))

    # Convert the transformed image to RGB for displaying
    transformed_img_rgb = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)

    # Show the transformed image
    plt.figure()
    plt.imshow(transformed_img_rgb)
    plt.title('Transformed Image')
    plt.axis('off')  # Hide axis
    plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()