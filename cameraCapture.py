# code to continuously live stream from camera
# press x to stop camera capture

# import OpenCV
import cv2

# initialize video capture object
capture = cv2.VideoCapture(0)

while True:
    # take the use of video camera for live stream capture
    unusedVariable, frame = capture.read()

    # display the video frame
    cv2.imshow('camera', frame)

    # break statement to end while loop (press x to end loop)
    if cv2.waitKey(1) == ord('x'):
        break

# release the use of video camera
capture.release()

# collapse the video capture window
cv2.destroyAllWindows()
