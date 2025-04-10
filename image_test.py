import face_recognition

# Load a sample picture
image = face_recognition.load_image_file("your_image.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

print(f"Found {len(face_locations)} face(s) in this image.")
