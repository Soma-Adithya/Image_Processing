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

##skeletonization
img = binary_image
# Function to perform iterative skeletonization
size = np.size(img)
skel = np.zeros(img.shape,np.uint8) 
ret,img = cv2.threshold(img,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy() 
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
cv2.imshow("skel",skel)
cv2.waitKey(0)
cv2.destroyAllWindows

