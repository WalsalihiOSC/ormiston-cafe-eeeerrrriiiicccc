from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Ormiston Cafe")
root.geometry("500x500")

# Create tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=5)

# Create two frames
currency_frame = Frame(notebook, width=480, height=480)
conversion_frame = Frame(notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

class OrmistonCafepg1:
    def __init__(self, parent):
        self.parent = parent

    home = LabelFrame(currency_frame, text="Order Now")
    home.pack(pady=20)
    
    home_button = Button(home, font=("Helvetica", 24))
    home_button.pack(pady=10, padx=10)

class OrmistonCafepg2:
    def __init__(self, parent):
        self.parent = parent

    home = LabelFrame(currency_frame, text="Order Now")
    home.pack(pady=20)

    home_button = Button(home, font=("Helvetica", 24))
    home_button.pack(pady=10, padx=10)

class OrmistonCafepg3:
    def __init__(self, parent):
        self.parent = parent

    home = LabelFrame(currency_frame, text="Order Now")
    home.pack(pady=20)

    home_button = Button(home, font=("Helvetica", 24))
    home_button.pack(pady=10, padx=10)

root.mainloop()
