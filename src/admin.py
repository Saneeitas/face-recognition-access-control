import tkinter as tk
from tkinter import messagebox
import json

def load_users():
    with open("data/users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("data/users.json", "w") as file:
        json.dump(users, file, indent=4)

def approve_user(user_id):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user["is_approved"] = True
            save_users(users)
            messagebox.showinfo("Success", f"User {user['name']} approved.")
            return
    messagebox.showwarning("Error", "User not found.")

def remove_user(user_id):
    users = load_users()
    users = [user for user in users if user["id"] != user_id]
    save_users(users)
    messagebox.showinfo("Success", "User removed successfully.")

def create_admin_gui():
    root = tk.Tk()
    root.title("Admin Panel")

    # Set window size
    window_width = 300
    window_height = 400

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(root, text="Registered Users", font=("Helvetica", 16)).pack(pady=10)

    users = load_users()
    user_listbox = tk.Listbox(root, width=50)
    user_listbox.pack(pady=10)

    for user in users:
        status = "Approved" if user["is_approved"] else "Pending"
        user_listbox.insert(tk.END, f"{user['id']}: {user['name']} ({status})")

    def approve_selected():
        selection = user_listbox.curselection()
        if selection:
            user_id = int(user_listbox.get(selection[0]).split(":")[0])
            approve_user(user_id)
            update_user_list(user_listbox)

    def remove_selected():
        selection = user_listbox.curselection()
        if selection:
            user_id = int(user_listbox.get(selection[0]).split(":")[0])
            remove_user(user_id)
            update_user_list(user_listbox)

    def update_user_list(listbox):
        listbox.delete(0, tk.END)
        for user in load_users():
            status = "Approved" if user["is_approved"] else "Pending"
            listbox.insert(tk.END, f"{user['id']}: {user['name']} ({status})")

    tk.Button(root, text="Approve User", command=approve_selected).pack(pady=5)
    tk.Button(root, text="Remove User", command=remove_selected).pack(pady=5)

    root.mainloop()