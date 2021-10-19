# OpenCV Tutorial 1

# cv2 is cv in this file
import cv2 as cv

# 1. Reading images

# Create img object using cv.imread(image_directory)
img = cv.imread('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/images/cat_large.jpeg')

# Show the img object in a HighGUI window named Cat
cv.imshow('Cat', img)

# Close the window on any keypress
cv.waitKey(0)


# 2. Reading videos

# In VideoCapture(), the parameter takes in 0, 1, 2, 3, ... as camera inputs, 0 is facecam, and more are just extra cams
# Create a videocapture object
capture = cv.VideoCapture('/Users/jkkim/Documents/PycharmProjects/testingOpenCV/videos/dog.mp4')

while True:
    # isTrue is true while the video has frames left, frame is each frame in the video
    isTrue, frame = capture.read()
    # Display each frame (which is an image and that is why we use imshow)
    cv.imshow('Video', frame)

    # waitKey(n) -> if n <= 0, run indefinitely until any keypress, if larger just displays the image for n ms.
    # For this example, the smaller the parameter is, the faster the video plays.
    # 0xFF because getting the first 256bits (0, 255), which is the first letter. Prevents numlock key from getting in the way
    # because numlock key adds a BIG number in binary, which results in a different ord value
    if cv.waitKey(5) & 0xFF == ord('d'):
        break

# Think of it as closing scanners in java.
capture.release()
# Destroy all HighGUI windows. In this case, you can use destroyWindow('Video'), which is a specified version.
cv.destroyAllWindows()

# When you run the script and see the end of the video, you will see an error named -215 Assertion fail; this means the
# video ran out of frames or finished and the program did not expect that. Think of it as index out of bounds error.
# Same error is raised when the file is not found either.





# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press ⌘F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/