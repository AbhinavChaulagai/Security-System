import tkinter as tk
from tkinter import messagebox
import cv2
import time

SECURITY_KEY = "1234"

root = tk.Tk()
root.title("Security Check")
root.geometry("300x150")

def capture_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam.")
        return

    ret, frame = cap.read()
    if ret:
        filename = f"user_image_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
        messagebox.showinfo("Photo Captured", f"Photo saved as {filename}")
    else:
        messagebox.showerror("Error", "Failed to capture image.")

    cap.release()
    cv2.destroyAllWindows()

def validate_key():
    entered_key = entry.get()
    if entered_key == SECURITY_KEY:
        messagebox.showinfo("Access Granted", "Welcome!")
        root.destroy()
    else:
        messagebox.showwarning("Access Denied", "Incorrect Security Key!")
        lock_window()

def lock_window():
    entry.config(state="disabled")
    button.config(state="disabled")
    capture_photo()

label = tk.Label(root, text="Enter Security Key:")
label.pack(pady=10)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)
button = tk.Button(root, text="Submit", command=validate_key)
button.pack(pady=10)

root.mainloop()
