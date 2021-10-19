# OpenCV Tutorial 8

import cv2 as cv
import numpy as np

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/park.jpeg')
cv.imshow('Boston', img)

# BGR is a result of blue, green, and red channels merged together.
# OpenCV allows us to split and merge color channels.

# 1. Splitting

b, g, r = cv.split(img)

# These images are split and shown as grayscale images. The brightness indicates the intensity of each color channel.
# For example, if you look at the Blue image, you can see how the sky is bright (there are a lotta blue pixels there,)
# But the trees are dark (there are little to no blue pixels there.)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Printing the images' shapes, the third element of the tuple indicates the number of color channels.
# You can't see anything for the b, g, r images because they each have 1.
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# 2. Merging

# Use a list of images-to-be-merged here
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# You can actually see the colors of the split images without it being grayscale.
# What you have to do is draw it on a blank images created through NumPy.
blank = np.zeros(img.shape[:2], dtype='uint8')

# Blank does not have 3 color channels; therefore, we have to merge the color channel with 2 other being blank so
# essentially simulate BGR, except that blank has the color of black which would result in only that color showing.
blue = cv.merge([b, blank, blank])
cv.imshow('Blue Only', blue)
green = cv.merge([blank, g, blank])
cv.imshow('Green Only', green)
red = cv.merge([blank, blank, r])
cv.imshow('Red Only', red)

cv.waitKey(0)
