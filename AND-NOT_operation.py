import cv2

#reading images
binary_img1 = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\black-and-white_image1.jpg")
binary_img2 = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\black-and-white_image2.jpg")

#resizing images
resized_img1 = cv2.resize(binary_img1, (500,500))
resized_img2 = cv2.resize(binary_img2, (500,500))

#Convert color image to gray scale image
grayscale1 = cv2.cvtColor(resized_img1, cv2.COLOR_BGR2GRAY)
grayscale2 = cv2.cvtColor(resized_img2, cv2.COLOR_BGR2GRAY)

#convert gray scale image to binary image
(thresh, Binary_image1) = cv2.threshold(grayscale1, 125, 255, cv2.THRESH_BINARY)
(thresh, Binary_image2) = cv2.threshold(grayscale2, 125, 255, cv2.THRESH_BINARY)

#Final and-not operation image
not_Binary_image1 = cv2.bitwise_not(Binary_image1, mask=None)
resultant = cv2.bitwise_and(not_Binary_image1,Binary_image2, mask=None)
cv2.imshow('AND-NOT',resultant)
cv2.waitKey(0)
cv2.destroyAllWindows()

