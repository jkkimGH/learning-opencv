# OpenCV Tutorial 13

import cv2 as cv

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')
cv.imshow('Cats', img)

# Thresholding: a binary realization of an image - if a pixel's intensity is less than the threshold, set it equal to
#               black, or 0. If greater, set it to white, or 1.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# 1. Simple Thresholding

# Returns the threshold value (150) as threshold_value & the converted image as thresh
threshold_value, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

# Inverse version
threshold_value, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Simple Thresholding', thresh_inverse)


# 2. Adaptive Thresholding
# Simple Thresholding has a downside where you have to define a value every time; this won't work in many cases.
# Adaptive Thresholding lets the computer do the job for you by finding the optimal threshold value on its own!

# Last param here -> c, used as (average of a kernal window) - c, which lets us fine tune.
#                                          max value                                     ~kernal size
#                                             |                                                |
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
# Inverse works too, just cv.THRESH_BINARY -> cv.THRESH_BINARY_INV
# Try the Gaussian method (cv.ADAPTIVE_THRESH_GAUSSIAN_C)

cv.waitKey(0)
