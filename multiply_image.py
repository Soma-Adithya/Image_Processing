import cv2
#Reading images
image1 = cv2.imread(r'C:\Users\somaa\Desktop\DIP Lab\DIP week 1.jpg')
image2 = cv2.imread(r'C:\Users\somaa\Desktop\DIP Lab\nature.jpg')
#Resizing images to equal size
image1=cv2.resize(image1,(500,500))
image2=cv2.resize(image2,(500,500))
#multiply images
result = cv2.multiply(image1,image2)
#showing image
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
