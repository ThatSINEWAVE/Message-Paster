import json
import tkinter as tk
from tkinter import messagebox, simpledialog, Scale
import keyboard
import pyautogui
import time
import threading

CONFIG_FILE = "keybinds.json"
MESSAGES_FILE = "messages.json"

def load_keybinds():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def load_messages():
    try:
        with open(MESSAGES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

keybinds = load_keybinds()
messages = load_messages()
typing_speed = 0.001

def send_message(text):
    pyautogui.write(text, interval=typing_speed)

def assign_key(message_name):
    new_key = simpledialog.askstring("Assign Key", f"Press a key for '{message_name}':")
    if new_key and new_key not in keybinds.values():
        keybinds[message_name] = new_key
        with open(CONFIG_FILE, "w") as file:
            json.dump(keybinds, file, indent=4)
        update_buttons()
        setup_hotkeys()
    elif new_key:
        messagebox.showwarning("Duplicate Key", "This key is already assigned.")

def setup_hotkeys():
    keyboard.unhook_all()
    for message, key in keybinds.items():
        keyboard.add_hotkey(key, lambda msg=messages.get(message, ""):
                          threading.Thread(target=send_message, args=(msg,)).start())

def update_buttons():
    for widget in frame.winfo_children():
        widget.destroy()
    for msg_name in messages.keys():
        key = keybinds.get(msg_name, "Not Set")
        btn = tk.Button(frame, text=f"{msg_name} ({key})", command=lambda m=msg_name: assign_key(m),
                       font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
        btn.pack(pady=5, fill=tk.X)

def update_speed(val):
    global typing_speed
    typing_speed = float(val)

root = tk.Tk()
root.title("Message Keybinder by ThatSINEWAVE")
root.geometry("400x600")
root.resizable(False, False)  # Disable both horizontal and vertical resizing
root.configure(bg="#333")

title_label = tk.Label(root, text="Message Keybinder", font=("Arial", 14, "bold"), fg="white", bg="#333")
title_label.pack(pady=10)

speed_frame = tk.Frame(root, bg="#333")
speed_frame.pack(pady=10)

speed_label = tk.Label(speed_frame, text="Typing Delay (seconds):", font=("Arial", 10), fg="white", bg="#333")
speed_label.pack()

speed_scale = Scale(speed_frame, from_=0.001, to=0.1, orient="horizontal", resolution=0.001,
                   command=update_speed, length=200, bg="#4CAF50", fg="white")
speed_scale.set(typing_speed)
speed_scale.pack()

speed_note = tk.Label(speed_frame, text="Lower = Faster (0.001 to 0.1)", font=("Arial", 8), fg="white", bg="#333")
speed_note.pack()

frame = tk.Frame(root, bg="#333")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

update_buttons()
setup_hotkeys()

root.mainloop()