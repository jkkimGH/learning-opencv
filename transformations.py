# OpenCV Tutorial 5

import cv2 as cv
import numpy as np

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/park.jpeg')

cv.imshow('Boston', img)

# 1. Translation

def translate(img, x, y):
    # Create a translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # Tuple of x and y of the image
    dimensions = (img.shape[1], img.shape[0])

    # Use Affine Transformation, which, in essence, represents a relation between two images.
    # Affine Transformation can express:
    #   1. Translations (vector addition)
    #   2. Rotations (linear transformation)
    #   3. Scale operations (linear transformation)

    #                    src   matrix  dimension size
    return cv.warpAffine(img, transMat, dimensions)

# If you have a negative x, you are translating the image to the left
# " negative y, " up
# " x, " to the right
# " y, " down

translated = translate(img, 100, 100)

cv.imshow('Translated', translated)

# 2. Rotation (usually around the center but here you also have the option to specify any point)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Positive angle -> rotate to the left
# Negative angle -> rotate to the right
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Doing this will cause parts of the image to be replaced by black triangles.
# This happens because when you rotate the image and there are nothing in the place where the picture used to be,
# And they replace it with just black pixels and it stays there.
# So when you rotate it again, the black pixels rotate together as well.
# If you don't want this to happen, just use it once with the angle you want: ex. use 90 instead of 2 45's
rotatedx2 = rotate(rotated, 45)
cv.imshow('Rotatedx2', rotatedx2)

# 3. Flipping

# 0 is flipping over the x-axis (vertical axis)
# 1 is y-axis (horizontally)
# -1 is over both axes
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

cv.waitKey(0)
