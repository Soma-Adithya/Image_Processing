import cv2
import numpy as np

#Convert image to noisy image with salt and pepper.
image = cv2.imread(r"C:\Users\somaa\Desktop\DIP Lab\DIP week 1.jpg") 
image = cv2.resize(image,(400,400))
noise_probability = 0.02 
salt_pepper_mask = np.random.rand(*image.shape[:2])
# Add salt noise (white pixels)
image[salt_pepper_mask < noise_probability] = [255, 255, 255]  # White
# Add pepper noise (black pixels)
image[salt_pepper_mask > 1 - noise_probability] = [0, 0, 0]  # Black


# Define a 9x9 averaging filter
kernel = np.ones((9, 9), np.float32) / (9*9)

# Apply the filter
filtered_image = cv2.filter2D(image, -1, kernel)

# Save the filtered image
cv2.imshow('Noisy Image', image)
cv2.imshow('averaging_filtered_image', filtered_image)
cv2.waitKey(0)



