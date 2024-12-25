import cv2
import numpy as np
import json
from tkinter import messagebox
import tkinter as tk
import sys

def load_recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("models/recognizer.yml")  # Adjust path if necessary
    return recognizer

def recognize_faces():
    recognizer = load_recognizer()
    with open("data/users.json", "r") as file:
        users = json.load(file)

    cap = cv2.VideoCapture(0)  # Open the camera
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    recognized_users = set()  # Track recognized users

    def on_closing():
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()  # Exit the application

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window close event

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray)

        for (x, y, w, h) in faces:
            id_, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            name = next((user['name'] for user in users if user['label'] == id_), "Unknown")

            if confidence < 100:
                if name not in recognized_users:
                    messagebox.showinfo("Recognition Result", f"Welcome {name}")
                    recognized_users.add(name)  # Add to recognized set
            else:
                # Show warning for non-registered users but do not exit
                if "Non-registered user" not in recognized_users:
                    messagebox.showwarning("Recognition Result", "Non-registered user")
                    recognized_users.add("Non-registered user")  # Track this message

            cv2.putText(frame, name if name != "Unknown" else "Unknown",
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    on_closing()  # Release resources on exit

def detect_faces(gray):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    return face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if __name__ == "__main__":
    recognize_faces()