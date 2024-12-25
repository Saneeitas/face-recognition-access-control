import os
from utils.detect_faces import detect_faces
from utils.train_recognizer import train_recognizer
import json

# Ensure necessary directories and files exist
os.makedirs("data/images", exist_ok=True)
if not os.path.exists("data/users.json"):
    with open("data/users.json", "w") as f:
        json.dump([], f)

def main():
    print(os.getcwd())
    print("Starting Face Recognition System...")


    # Step 1: Detect faces (example usage)
    image_path = "data/images/image1.jpg"  # Replace with actual image
    num_faces, faces = detect_faces(image_path)
    print(f"Number of faces detected: {num_faces}")

    # Step 2: Add user data (Example: You can make this dynamic later)
    with open("data/users.json", "r+") as file:
        users = json.load(file)
        users.append({
            "id": len(users) + 1,
            "name": "John Doe",
            "image_path": image_path,
            "label": len(users) + 1,
            "is_approved": True
        })
        file.seek(0)
        json.dump(users, file, indent=4)

    # Step 3: Train recognizer
    train_recognizer()

if __name__ == "__main__":
    main()
