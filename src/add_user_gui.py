import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from utils.train_recognizer import train_recognizer

def add_user(name, image_path):
    with open("data/users.json", "r+") as file:
        users = json.load(file)
        users.append({
            "id": len(users) + 1,
            "name": name,
            "image_path": image_path,
            "label": len(users) + 1,
            "is_approved": True
        })
        file.seek(0)
        json.dump(users, file, indent=4)

def upload_image():
    filepath = filedialog.askopenfilename()
    if filepath:
        name = name_entry.get()
        if name:
            add_user(name, filepath)
            train_recognizer()  # Train the recognizer after adding the user
            messagebox.showinfo("Success", "User added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")

def create_gui():
    global name_entry
    root = tk.Tk()
    root.title("Add User")
    
    # Set window size
    window_width = 400
    window_height = 250
    
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate x and y coordinates to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(root, text="Name:").pack(pady=10)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=10)

    tk.Button(root, text="Upload Image", command=upload_image).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()