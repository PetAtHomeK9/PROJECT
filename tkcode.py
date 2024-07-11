import tkinter as tk

root = tk.Tk()

root.geometry("500x800")

root.title("PetAtHome K9")

label = tk.Label(root, image=, text="Fetch Me!", font=("Arial, 18"))
label.pack(padx= 20, pady= 100)
textbox = tk.Text(root, height= 1, font=("Arial, 16"))
textbox.pack()

root.mainloop()