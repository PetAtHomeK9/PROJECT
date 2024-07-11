import tkinter as tk

def create_button(root, text, bg, activebackground, foreground, command=None):
    button = tk.Button(
        root, 
        text=text, 
        bg=bg, 
        activebackground=activebackground, 
        foreground=foreground, 
        command=command
    )
    return button
