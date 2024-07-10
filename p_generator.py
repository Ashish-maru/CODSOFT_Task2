import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        complexity = complexity_var.get()
        
        password = generate_password(length, complexity)
        
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Invalid input", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='#e0f2f1')  # Set light blue background color

# Widgets
length_label = tk.Label(root, text="Enter the desired length of the password:", bg='#e0f2f1', fg='red', font=('Arial', 12))
length_label.pack(pady=15)

length_entry = tk.Entry(root, font=('Arial', 12), bg='#ffffff', fg='#333333')
length_entry.pack(pady=5)

complexity_label = tk.Label(root, text="Select password complexity:", bg='#e0f2f1', fg='blue', font=('Arial', 12))
complexity_label.pack(pady=10)

complexity_var = tk.StringVar()
complexity_var.set("medium")  # Default complexity level

complexity_frame = tk.Frame(root, bg='#e0f2f1')
complexity_frame.pack()

low_radio = tk.Radiobutton(complexity_frame, text="Low", variable=complexity_var, value="low", bg='#e0f2f1')
low_radio.grid(row=0, column=0, padx=10)

medium_radio = tk.Radiobutton(complexity_frame, text="Medium", variable=complexity_var, value="medium", bg='#e0f2f1')
medium_radio.grid(row=0, column=1, padx=10)

high_radio = tk.Radiobutton(complexity_frame, text="High", variable=complexity_var, value="high", bg='#e0f2f1')
high_radio.grid(row=0, column=2, padx=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui, bg='#00bcd4', fg='#ffffff', font=('Arial', 12))
generate_button.pack(pady=20)

password_label = tk.Label(root, text="Generated password:", bg='#e0f2f1', fg='green', font=('Arial', 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, state=tk.DISABLED, font=('Arial', 12), bg='#ffffff', fg='#333333')
password_entry.pack(pady=5)

# Run the application
root.mainloop()
