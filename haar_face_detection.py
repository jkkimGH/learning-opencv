# OpenCV Face Detection: Haar Cascade

# Face Detection != Face Recognition. FD only knows if a face is present in the image or not.
# It also uses grayscale images, so no color tone is considered.
# Haar Cascade looks at the edges of the objects within the images to determine whether a face is present or not.

# Local Binary Patterns (not here, but it's also good)

import cv2 as cv

# Photo face detection

# img = cv.imread('../../../Downloads/noMask.jpg')
# cv.imshow('People', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)

# Creating a haar cascade object
haar_cascade = cv.CascadeClassifier('haar_cascade_face.xml')

# Returns a list of coordinates of faces found
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# print(f'Number of faces found = {len(faces_rect)}')


# Webcam face detection

webcam = cv.VideoCapture(0)

while True:
    isTrue, frame = webcam.read()
    cv.imshow('Webcam', frame)

    graycam = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(graycam, scaleFactor=1.1, minNeighbors=3)
    print(f'Number of faces found = {len(faces_rect)}')

    if cv.waitKey(5) & 0xFF == ord('d'):
        break

webcam.release()
cv.destroyAllWindows()

cv.waitKey(0)
