# OpenCV Tutorial 7

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/park.jpeg')
cv.imshow('Boston', img)

# Showing the difference in color representation between RGB and BGR, uncomment these two lines
plt.imshow(img)
plt.show()

# Color spaces

# 1. BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# NOTE: You cannot directly convert a grayscale image into a HSV image.
#       To do this, you have to convert grayscale -> BGR -> HSV
#       Same for other color spaces, just use the appropriate cv.COLOR_ command

# 2. BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. BGR to LAB or L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR is not the conventional method used to display the colors of an image - RGB is.
# Because OpenCV uses BGR, if you try opening the image in a Python script without OpenCV,
# you're going to see an inversion of the colors.

# 4. BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Showing the converted image (BGR -> RGB) through matplotlib
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
