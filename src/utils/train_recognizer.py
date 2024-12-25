import cv2
import numpy as np
import json

def train_recognizer():
    images, labels = [], []

    # Load user data from JSON
    with open("../src/data/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["is_approved"]:
            image_path = user["image_path"]
            label = user["label"]

            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(label)

    # Train recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(images, np.array(labels))
    recognizer.save("../src/models/recognizer.yml")
    print("Recognizer trained and saved.")
