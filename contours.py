# OpenCV Tutorial 6

import cv2 as cv
import numpy as np

# Contours are basically the boundaries of an object. However, in a mathematical POV, these are not the same as edges.
# But in programming, you can get away with thinking contours as edges because they are sort of the edges of the image
# - They are the curves that join the points along the boundaries
# Contours ae very useful when it comes to shape analysis, object detection & recognition.

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')

cv.imshow('Cats', img)

# 5. You can essentially draw over the contours of the images to visualize them

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
# Find more on this at the bottom


# 1. Convert to grayscale image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Can: blur the image a bit to reduce unnecessary contours and reduce the size of the output
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 2. Grab the edges of the image using the Canny edge detector

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# 4. Instead of using Canny edge detector, you can also use threshold

# threshold basically looks at the image and tries to binary-ize the it.
# If a pixel is below the intensity of 125, it turns it into intensity 0 (black), and the others intensity 255 (white)
# Don't worry too much about this for now
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# 3. Use the findContours method

# Some modes:
# 1. RETR_TREE if you want all hierarchical contours
# 2. RETR_EXTERNAL for only external contours
# 3. RETR_LIST for ALL contours.

# Some methods: how we want to approximate the contours
# 1. CHAIN_APPROX_NONE returns all contours, does nothing
# 2. CHAIN_APPROX_SIMPLE compresses all the contours that are returned into a simple one that makes the most sense

#                                       image      mode            method
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# HOW IT WORKS:
# 1. findContours looks at the structuring element/edges found in the image
# 2. returns 2 values: contours (list of all contours' coordinates found in the image)
#                      hierarchies (refers to the hierarchical representation of the contours)

print(f'{len(contours)} contour(s) found!')

# We're drawing contours! (Actually, it just traced over the edges of the threshold image)
# drawContours(image, contours_list, how_many_contours (-1 if all), color (BGR), thickness)
cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours Drawn', blank)

# IMPORTANT: when trying to find contours, try the Canny method first
#            because they're usually more reliable and threshold has its disadvantages.

cv.waitKey(0)
