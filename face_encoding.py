import face_recognition
import cv2
import os
import numpy as np
import pickle

# Path to the dataset folder
dataset_dir = 'dataset'
known_encodings = []
known_names = []

# Loop through each person's folder
for person_name in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_name)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        image = cv2.imread(img_path)
        
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

# Save the encodings and names
data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encodings saved successfully!")
