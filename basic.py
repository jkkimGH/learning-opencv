# OpenCV Tutorial 4

import cv2 as cv

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/park.jpeg')
cv.imshow('Park', img)

# 1. img is a BGR image. Let's convert it to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur

# Second parameter is 'kernal size': 2x2 tuple that is used as a window size that opencv uses to blur the image.
# We'll learn more later. Just keep in mind that the values have to be odd numbers. The bigger the numbers, the blurrier.
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade: finding edges present in the image

# Canny is a famous edge detector in the CV world
#             threshold 1 threshold 2
# The higher the threshold, the more abstract
# Also can use blurred image to get less edges
canny = cv.Canny(img, 200, 250)
cv.imshow('Edges', canny)

# 4. Dilating the image: thickens the edges in this case
# This is a structuring element

#                        kernel size
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# 5. Eroding - sorta reverse of cv.dilate()

#                        kernal size
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# 6. Resize

#              resized size ignoring aspect ratio
#                                    cv.INTER_AREA is useful when shrinking
#                                    cv.INTER_LINEAR for enlarging
#                                    cv.INTER_CUBIC is the slowest but gives the best quality
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# 7. Cropping: utilizing the fact that the images are arrays

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
