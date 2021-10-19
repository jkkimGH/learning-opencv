# OpenCV Tutorial 10

import cv2 as cv
import numpy as np

# Bitwise operators AND OR XOR NOT are used a lot in image processing.
# (especially when working with masks, see next tutorial)
# At a high level, bitwise operators operate in a binary manner: 0 = off, 1 = on.

blank = np.zeros((400, 400), dtype='uint8')

# Fourth param = color, 0-255 since binary image
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# 1. Bitwise AND (intersecting regions)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# 2. Bitwise OR (intersecting and non-intersecting regions)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# 3. Bitwise XOR (non-intersecting regions)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# 4. Bitwise NOT (inverts the binary colors)

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT', bitwise_not)

cv.waitKey(0)
