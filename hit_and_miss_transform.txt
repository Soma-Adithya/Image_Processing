#Use binary image
import cv2
import numpy as np

###Convert color image to binary image
# Read the input color image
color_image = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\DIP week 1.jpg")
color_image = cv2.resize(color_image,(500,500))
# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
# Set a threshold value (adjust as needed)
threshold_value = 128
# Apply binary thresholding
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary",binary_image)

##HIT AND MISS TRANSFORM
image = binary_image
# Define the object and background structuring elements
object_kernel = np.array([[0, 1, 0],
                          [1, 1, 1],
                          [0, 1, 0]], dtype=np.uint8)

background_kernel = np.array([[1, 0, 1],
                              [0, 0, 0],
                              [1, 0, 1]], dtype=np.uint8)
# Apply the hit-and-miss transform
result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, object_kernel, None, iterations=1)
result = cv2.morphologyEx(result, cv2.MORPH_HITMISS, background_kernel, None, iterations=1)
cv2.imshow('HIT AND MISS TRANSFORM', result)
cv2.waitKey(0)
cv2.destroyAllWindows
