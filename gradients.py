# OpenCV Tutorial 14

import cv2 as cv
import numpy as np

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')
cv.imshow('Cats', img)

# Gradients and Edge Detection

# In math, gradients and edges are completely different things - but in programming, you can sorta get away with
# treating them the same

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# 1. Laplacican

lap = cv.Laplacian(gray, cv.CV_64F)
# Basically, we're converting the image from black to white then white to black,
# which is considered a positive and negative slope.
# However, since pixels can't have negative values, we just put an absolute value over it.
# Then, we convert the image into an uint8 datatype (image specific)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
# Shows the Laplacian edges

# 2. Sobel Gradient Magnitude Representation

# Computes gradients into two directions, x and y.

# Third & fourth param = x & y direction
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Using Canny edge detector to compare Laplacian and Sobel

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
# As you remember, Canny is an advanced multi-stage algorithm - canny uses Sobel in one of the stages.
# Canny is used a lot generally, but Sobel is used quite a bit in more advanced settings.

cv.waitKey(0)
