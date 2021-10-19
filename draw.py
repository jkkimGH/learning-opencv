# OpenCV Tutorial 3

import cv2 as cv
import numpy as np

# Creating a blank window to draw on with numpy
# Give it a shape tuple length of 3: first two are height and width.
# The last is the number of color channels, in this case BGR (Blue Green Red)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color

# The order is BGR not RGB
blank[:] = 212, 255, 127
# Set range (area) where it is a certain color
#     y1 to y2 x1 to 2    color
# The y-axis is horizontal and x is vertical. Origin is a the top left corner.
blank[200:300, 200:300] = 0, 255, 0
cv.imshow('Teal and Green Sq', blank)

# 2. Create a rectangle (not filled)

#                     y1  x1      y2   x2                                   color   thickness=cv.FILLED or -1 for fill
#                 can do blank.shape[1 or 0]//n to scale down the x or y by n (based off the window)
cv.rectangle(blank, (200, 200), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=2)
cv.imshow('Combo', blank)

# 3. Create a circle (not filled)

#                  center  radius    color
cv.circle(blank, (300, 300), 50, (0, 255, 255), thickness=-1)
cv.imshow('Art', blank)

# 4. Create a line

#        starting point   end point      color
cv.line(blank, (300, 50), (250, 450), (145, 0, 0), thickness=2)
cv.imshow('Abstract', blank)

# 5. Write text

cv.putText(blank, 'What\'s up', (150, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (250, 250, 250), thickness=1)
cv.imshow('BOOM', blank)

cv. waitKey(0)
