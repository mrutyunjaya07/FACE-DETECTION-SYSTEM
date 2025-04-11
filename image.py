import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import subprocess

# Folder where images are stored
IMAGE_DIR = "ImagesAttendance"
CSV_FILE = "Attendance.csv"

# Make sure image folder exists
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# GUI Functions
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
    if file_path:
        name = os.path.splitext(os.path.basename(file_path))[0]
        dest_path = os.path.join(IMAGE_DIR, name + ".jpg")
        shutil.copy(file_path, dest_path)
        messagebox.showinfo("Success", f"Image saved as {dest_path}")

def start_attendance():
    subprocess.run(["python", "attandance_with_photo.py"])

def open_csv():
    if os.path.exists(CSV_FILE):
        os.startfile(CSV_FILE)
    else:
        messagebox.showerror("Error", "Attendance file not found.")

# GUI Window
root = tk.Tk()
root.title("Face Attendance System")
root.geometry("400x300")
root.config(bg="#e6f2ff")

title = tk.Label(root, text="Face Attendance System", font=("Helvetica", 16, "bold"), bg="#e6f2ff")
title.pack(pady=20)

btn_upload = tk.Button(root, text="Upload Student Image", width=25, command=upload_image)
btn_upload.pack(pady=10)

btn_start = tk.Button(root, text="Start Attendance", width=25, command=start_attendance)
btn_start.pack(pady=10)

btn_csv = tk.Button(root, text="Open Attendance CSV", width=25, command=open_csv)
btn_csv.pack(pady=10)

root.mainloop()
