# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 11:00:35 2026

@author: Ansari
"""

import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate a key (in real-world use, save this securely!)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_text():
    plaintext = entry_text.get("1.0", tk.END).strip()
    if not plaintext:
        messagebox.showwarning("Warning", "Please enter some text to encrypt.")
        return
    encrypted = cipher_suite.encrypt(plaintext.encode())
    entry_result.delete("1.0", tk.END)
    entry_result.insert(tk.END, encrypted.decode())

def decrypt_text():
    ciphertext = entry_text.get("1.0", tk.END).strip()
    if not ciphertext:
        messagebox.showwarning("Warning", "Please enter some text to decrypt.")
        return
    try:
        decrypted = cipher_suite.decrypt(ciphertext.encode())
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decrypted.decode())
    except Exception:
        messagebox.showerror("Error", "Invalid ciphertext or wrong key!")

# GUI setup
root = tk.Tk()
root.title("Cybersecurity Beginner Project - Encryption/Decryption")
root.geometry("600x400")

label1 = tk.Label(root, text="Enter Text:", font=("Arial", 12))
label1.pack(pady=5)

entry_text = tk.Text(root, height=5, width=60)
entry_text.pack(pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="Encrypt", command=encrypt_text, bg="lightblue", width=15)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="Decrypt", command=decrypt_text, bg="lightgreen", width=15)
btn_decrypt.grid(row=0, column=1, padx=10)

label2 = tk.Label(root, text="Result:", font=("Arial", 12))
label2.pack(pady=5)

entry_result = tk.Text(root, height=5, width=60, bg="#f0f0f0")
entry_result.pack(pady=5)

root.mainloop()