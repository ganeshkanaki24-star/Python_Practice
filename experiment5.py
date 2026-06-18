from tkinter import *
from tkinter import messagebox

# Create window
root = Tk()
root.title("Registration Form")
root.geometry("500x550")
root.config(bg="#f0f0f0")

# Title Label
title = Label(root, text="Registration Form", font=("Arial", 22, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# ====== Functions ======
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    gender = gender_var.get()
    password = entry_password.get()

    if name == "" or email == "" or phone == "" or gender == "" or password == "":
        messagebox.showerror("Error", "All Fields Are Required!")
    else:
        messagebox.showinfo("Success", "Registration Successful!")
        clear_form()

def clear_form():
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    entry_phone.delete(0, END)
    entry_password.delete(0, END)
    gender_var.set("")

# ====== Labels & Entry Fields ======

label_font = ("Arial", 14)
entry_font = ("Arial", 13)

# Name
Label(root, text="Full Name", font=label_font, bg="#f0f0f0").pack(pady=5)
entry_name = Entry(root, font=entry_font, width=30)
entry_name.pack(pady=5)

# Email
Label(root, text="Email", font=label_font, bg="#f0f0f0").pack(pady=5)
entry_email = Entry(root, font=entry_font, width=30)
entry_email.pack(pady=5)

# Phone
Label(root, text="Phone Number", font=label_font, bg="#f0f0f0").pack(pady=5)
entry_phone = Entry(root, font=entry_font, width=30)
entry_phone.pack(pady=5)

# Gender
Label(root, text="Gender", font=label_font, bg="#f0f0f0").pack(pady=5)

gender_var = StringVar()

frame_gender = Frame(root, bg="#f0f0f0")
frame_gender.pack()

Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male", font=("Arial", 12), bg="#f0f0f0").pack(side=LEFT, padx=10)
Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female", font=("Arial", 12), bg="#f0f0f0").pack(side=LEFT, padx=10)

# Password
Label(root, text="Password", font=label_font, bg="#f0f0f0").pack(pady=5)
entry_password = Entry(root, font=entry_font, width=30, show="*")
entry_password.pack(pady=5)

# Buttons
btn_frame = Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

Button(btn_frame, text="Submit", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=10, command=submit_form).pack(side=LEFT, padx=10)
Button(btn_frame, text="Clear", font=("Arial", 14, "bold"), bg="#f44336", fg="white", width=10, command=clear_form).pack(side=LEFT, padx=10)

# Run window
root.mainloop()
