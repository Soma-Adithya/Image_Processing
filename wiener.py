import cv2
import numpy as np
import scipy.signal

image = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\DIP week 1.jpg")
image = cv2.resize(image,(400,400))
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

weiner_image = scipy.signal.wiener(image,(3,3),noise = None)
result = np.uint8(weiner_image)

cv2.imshow("result",result)
cv2.waitKey(0)
