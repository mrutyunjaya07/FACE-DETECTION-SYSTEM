 # Import the OpenCV library
import cv2 

# Start capturing video from the default camera (0 is usually the built-in webcam)
video = cv2.VideoCapture(1)

while True:
    # Read a frame from the webcam
    ret, frame = video.read()

    # Display the frame in a window named "Test Webcam"
    cv2.imshow("Test Webcam", frame)

    # Wait for 1 millisecond and check if the 'q' key was pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam resource
video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
