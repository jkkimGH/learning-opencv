# OpenCV Tutorial 9

import cv2 as cv

img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cats.jpeg')
cv.imshow('Cats', img)

# Smoothing and blurring
# Smoothing the image by blurring helps eliminate/tone down some of the noise.

# Although the Gaussian blur is one of the most popular blurring methods, it won't always suit your needs.

# What goes on in the background while blurring an image?
#    Let's define what a kernel (or window) is: imagine a 3x3 grid window covering a part of the image.
#    in this case, the kernel size is 3x3 (rows x columns). When you blur, something happens to a pixel as a result of
#    its surrounding pixels (middle pixel changed due to the 8 surrounding pixels).

# Now, time to discuss the first method of blurring - Averaging.
# First, the program picks a portion of the image and defines a kernal window.
# Then, it computes and applies the average intensity of all surrounding pixels to the middle pixel (aka true center).
# Repeat throughout the image.

# The higher the kernal size, the more blur
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

# Now onto the Gaussian Blur:
# This is similar to the Average Blur, except that Gaussian uses a different method to calculate the true center value.
# Each surrounding pixel is given a weight, and the average of the products of the weights = value for the true center.
# This makes it so that you get less amount of but more natural looking blur than the Average Blur.

# The third parameter is sigmaX (standard deviation in the x-axis)
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# The Median Blur:
# The value of the true center is found by finding the median of the intensity of the surrounding pixels.
# Generally, the Median Blur is more effective than the Average Blur and even the Gaussian in reducing noise.
# This is used mainly in CV projects that depends on the removal of the substantial amount of noise.

# No need for a tuple for kernal size n here, OpenCV assumes that you will use a n x n tuple for it.
# Also, the Median Blur is not meant for a high kernal size like 5 as it's good at reducing some noise.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# The Bilateral Blur:
# The most effective, used in many advanced CV projects essentially because of how it blurs.
# The traditional blurring methods don't care where you are blurring. However, the Bilateral Blur does care,
# and helps retain the edges of the image.

# The second parameter is not a kernal size, but a diameter.
# The third parameter is the sigma color. The larger the value,
#   the more colors in the neighborhood that will be considered in computing the blur.
# The fourth parameter is the sigma space.
#   Larger value means further pixels from the true center will affect the blurring computation.

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

# IMPORTANT: keep in mind that both median and bilateral blurring are meant for small values;
#            large values will cause the images to look like they were smudged.

cv.waitKey(0)
