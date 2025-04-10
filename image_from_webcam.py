import cv2
import os

# Set the name of the person
person_name = "MJ"  # Change this for each person
save_dir = f"dataset/{person_name}"

# Create directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Start webcam
cap = cv2.VideoCapture(1)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use built-in OpenCV face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Save face if 's' is pressed
        if cv2.waitKey(1) & 0xFF == ord('s'):
            count += 1
            face_filename = os.path.join(save_dir, f"{person_name}_{count}.jpg")
            cv2.imwrite(face_filename, face)
            print(f"Saved: {face_filename}")

    cv2.imshow("Capture Faces - Press 's' to save, 'q' to quit", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
