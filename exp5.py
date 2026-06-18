import tkinter as tk
root= tk.Tk()
root.title("Button")
root.geometry("200x150")
#create button
button = tk.Button(root, text = "click me")
button.pack(pady=20)
root.mainloop()