# OpenCV Tutorial 2

import cv2 as cv

# 3. Image rescale function - works with image, video, and live video.

def rescaleFrame(frame, scale=0.75): # Default value of scale is 0.75, can change it to whatever you want
    # Basically, frame.shape[1] is the width and [0] is the height
    # Apply scaling
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # Create a tuple named dimensions
    dimensions = (width, height)

    # Resize the image and return
    # "INTER_AREA – resampling using pixel area relation.
    # It may be a preferred method for image decimation, as it gives moire'-free results.
    # But when the image is zoomed, it is similar to the INTER_NEAREST method."
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# 4. Changing image resolution - only works for live video

def changeRes(source, width, height):
    # 3 references the width and 4 references the height in the capture class.
    # This directly changes the capture object, so change 'capture' to whatever your object name is.
    source.set(3, width)
    source.set(4, height)


# Reusing the video example from last tutorial

capture = cv.VideoCapture('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/videos/dog.mp4')
webcam = cv.VideoCapture(0)

while True:
    #isTrue, frame = capture.read()
    # Rescale each frame using rescaleFrame method
    #frame_resized = rescaleFrame(frame, scale=.2) # Change the scale to what you want/need
    #cv.imshow('Video', frame)
    # Show the rescaled video
    #cv.imshow('Rescaled video', frame_resized)

    # The webcam experiment
    # Read from the webcam's input
    isTrue, frame = webcam.read()
    # Use changeRes to change the resolution (maybe works? idk)
    changeRes(webcam, 1280, 720)
    cv.imshow('Webcam', frame)

    if cv.waitKey(5) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
