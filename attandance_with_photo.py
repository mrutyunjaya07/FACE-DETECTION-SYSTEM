import face_recognition
import cv2
import numpy as np
import pickle
import pandas as pd
from datetime import datetime

# Load known face encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Attendance CSV filename (date-based)
today = datetime.now().strftime("%Y-%m-%d")
filename = f"Attendance_{today}.csv"

# Initialize attendance file
try:
    df = pd.read_csv(filename)
    recorded_names = df['Name'].tolist()
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    recorded_names = []

# Start webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matched_idxs = [i for i, b in enumerate(matches) if b]
            counts = {}

            for i in matched_idxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

        names.append(name)

    # Mark attendance
    for name in names:
        if name != "Unknown" and name not in recorded_names:
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            new_row = pd.DataFrame([{"Name": name, "Date": date_str, "Time": time_str}])
            df = pd.concat([df, new_row], ignore_index=True)
            recorded_names.append(name)
            df.to_csv(filename, index=False)
            print(f"Marked attendance for {name} at {time_str}")

    # Display
    for (top, right, bottom, left), name in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Face Recognition + Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
