import sys
import tkinter as tk
from tkinter import messagebox
import subprocess
from admin import create_admin_gui 

def open_registration():
    result = subprocess.run([sys.executable, "add_user_gui.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def start_recognition():
    result = subprocess.run([sys.executable, "face_recognition.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def admin_access():
    create_admin_gui()

def create_main_menu():
    root = tk.Tk()
    root.title("Face Recognition System")
    
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

    tk.Label(root, text="Welcome to the Face Recognition System", font=("Helvetica", 12)).pack(pady=10)

    tk.Button(root, text="Register User", command=open_registration, width=20).pack(pady=10)
    tk.Button(root, text="Scan Face", command=start_recognition, width=20).pack(pady=10)
    tk.Button(root, text="Admin Access", command=admin_access, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_menu()