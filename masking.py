# OpenCV Tutorial 11

import cv2 as cv
import numpy as np

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')
cv.imshow('Cats', img)

# Masking allows us to focus on certain parts of a image
# For example, if you wanted to focus on people's faces in an image containing many people,
# you could essentially mask over their faces and remove all the unwanted parts of them.

# Create a mask using numpy
# IMPORTANT: the dimensions of the mask have to be the same size as that of the image.
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# You can create weird shapes and use them as a mask, but here, (for simplicity) we use a circle.
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)

# Masking over the img and showing the intersection
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)

cv.waitKey(0)
