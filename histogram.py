# OpenCV Tutorial 12

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')
cv.imshow('Cats', img)

# Computing histograms
# Histograms allow you to visualize the distribution of the pixel intensities in an image.

# 1. Histograms for grayscale images

# Convert into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Create histogram
# First param = list of images to create histogram for, in this case only 1.
# Second param = number/index of channels we want to compute a histogram for, in this case 0 because grayscale
# Third param = mask to create a histogram for a specific part of the image, which for now is None.
# Fourth param = histSize, which is the number of bins we want to use for computing the histogram. More on this later
# Fifth param = range of all possible pixel values, in this case 0 ~ 256

# Commented to test histogram for masked image
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# 2. Using a mask for grayscale histogram
blank = np.zeros(gray.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)
mask = cv.circle(blank, (gray.shape[1] // 2, gray.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)
masked_img = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked Image', masked_img)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Create a matplotlib figure and display the histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# HOW TO INTERPRET THE HISTOGRAM: There are (y-value) pixels with intensity of (x-value),
#                                 where intensity is a color between black and white.

# 3. Histograms for RGB images

colors = ('b', 'g', 'r')

# 4. Using a mask for RGB histogram
# Copy paste previous code and change var names/param

blank2 = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank 2', blank2)
mask2 = cv.circle(blank2, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask 2', mask2)
masked_img2 = cv.bitwise_and(img, img, mask=mask2)
cv.imshow('Masked Image 2', masked_img2)

plt.figure()
plt.title('RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

# This for loop goes through the colors tuple and generates histogram for each color.
for i, clr in enumerate(colors):
    # To go between number 3 and 4, change mask2 to None and vice versa.
    rgb_hist = cv.calcHist([img], [i], mask2, [256], [0, 256])
    plt.plot(rgb_hist, color=clr)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
