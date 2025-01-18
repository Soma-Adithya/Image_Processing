import cv2

#Reading image
image = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\DIP week 1.jpg")
image1 = cv2.resize(image,(400,400))

#parameters and rotating
height,width = image1.shape[0:2]
angle = 270
T = cv2.getRotationMatrix2D((width//2,height//2),angle,1.0)
rotated_image = cv2.warpAffine(image1, T, (width,height))

#showing image
cv2.imshow("result", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows
