import tkinter as tk
from tkinter import messagebox
from tkinter import *
# Encrypt the message with Caesar Cipher
def encrypt_text():
    try:
        message = entry_message.get()
        key = int(entry_key.get())
        encrypted_text = ''.join(
            chr((ord(char) + key - 65) % 26 + 65) if char.isupper() else
            chr((ord(char) + key - 97) % 26 + 97) if char.islower() else char
            for char in message
        )
        entry_result.delete(0, tk.END)
        entry_result.insert(0, encrypted_text)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid key.")

# Decrypt the message with Caesar Cipher
def decrypt_text():
    try:
        message = entry_message.get()
        key = int(entry_key.get())
        decrypted_text = ''.join(
            chr((ord(char) - key - 65) % 26 + 65) if char.isupper() else
            chr((ord(char) - key - 97) % 26 + 97) if char.islower() else char
            for char in message
        )
        entry_result.delete(0, tk.END)
        entry_result.insert(0, decrypted_text)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid key.")

# Initialize GUI
root = tk.Tk()
img=PhotoImage(file='C:/Users/91830/Desktop/INTERNSHIP/pic.png')
root.iconphoto(False,img)
root.title("Encryption & Decryption Tool")
root.geometry("400x300")

# Message Input
tk.Label(root, text="Message:").pack(pady=5)
entry_message = tk.Entry(root, width=50)
entry_message.pack(pady=5)

# Key Input
tk.Label(root, text="Key (Shift Value):").pack(pady=5)
entry_key = tk.Entry(root, width=20)
entry_key.pack(pady=5)

# Encrypt/Decrypt Buttons
tk.Button(root, text="Encrypt", command=encrypt_text).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_text).pack(pady=5)

# Result Output
tk.Label(root, text="Result:").pack(pady=5)
entry_result = tk.Entry(root, width=50)
entry_result.pack(pady=5)

root.mainloop()
