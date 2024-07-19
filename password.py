import tkinter as tk
import string
import random

def generate_password():
    password = []
    for i in range(5):
        alp = random.choice(string.ascii_letters)
        num = random.choice(string.digits)
        sym = random.choice(string.punctuation)
        password.append(alp)
        password.append(num)
        password.append(sym)
        passwords = " ".join(str(x)for x in password)
        label.config(text=passwords)
root = tk.Tk()
root.geometry("400x300")
button = tk.Button(root, text="Generate Password", command=generate_password)
button.grid(row=1, column=1)
label = tk.Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=2)
root.mainloop()