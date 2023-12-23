from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

# Globalny słownik dla przechowywania obrazów
loaded_images = {}

class ToggleButton:
    def __init__(self, master, image1, image2, size, row, column, padx=0, pady=0, text="", chosenButton = 0):
        self.chosenButton = chosenButton
        self.master = master
        self.image1 = self.load_image(image1, size)
        self.image2 = self.load_image(image2, size)
        self.button = tk.Canvas(master, width=size[0], height=size[1], bg='#261717', bd=0, highlightthickness=0)
        self.image_on_canvas = self.button.create_image(0, 0, anchor=tk.NW, image=self.image1)
        self.button.create_text(size[0]//2, size[1]//2, text=text, fill="white", font=("Segoe UI", 20))
        self.button.grid(row=row, column=column, padx=padx, pady=pady)
        self.button.bind('<Button-1>', self.on_click)  
        self.button.bind('<ButtonRelease-1>', self.on_release)

    def button_click(self, number=0):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current)+str(number))

    def load_image(self, path, size):
        if path not in loaded_images:
            loaded_images[path] = ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))
        return loaded_images[path]

    def on_click(self,event):
        if self.chosenButton == 10:
            e.delete(0, END)
            self.button.itemconfig(self.image_on_canvas, image=self.image2)
        else:
            self.button_click(self.chosenButton)
            self.button.itemconfig(self.image_on_canvas, image=self.image2)

    def on_release(self, event):
        self.button.itemconfig(self.image_on_canvas, image=self.image1)


# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.configure(bg='#261717')
root.title('Kalkulator')
root.geometry('305x374')
root.resizable(False, False)
root.iconbitmap('D:/Python/tkinter/Images/icon.ico')

large_font = font.Font(family='Segoe UI', size=25)
global e 
e = tk.Entry(root, width=15, bg="#261717", fg="white", borderwidth=0, font=large_font, insertontime=0)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Ustawienia dla przycisków
button_size = (70, 70)
image1_path = 'D:/Python/tkinter/Images/button2.png'
image2_path = 'D:/Python/tkinter/Images/button.png'
button_equal1 = 'D:/Python/tkinter/Images/equal_button.png'
button_equal2 = 'D:/Python/tkinter/Images/equal_button2.png'

# Tworzenie przycisków
buttons = []
alpha = 1
for row in range(3):
    for column in range(3):
        button = ToggleButton(root, image1_path, image2_path, button_size, row+1, column, 3, 3, str(alpha),alpha)
        buttons.append(button)
        alpha += 1

multiply_button = ToggleButton(root, image1_path, image2_path, button_size, 1, 3, 3, 3, "x",0)
divide_button = ToggleButton(root, image1_path, image2_path, button_size, 2, 3, 3, 3, "/",0)
minus_button = ToggleButton(root, image1_path, image2_path, button_size, 3, 3, 3, 3, "-",0)
plus_button = ToggleButton(root, image1_path, image2_path, button_size, 4, 3, 3, 3, "+",0)
clear_button = ToggleButton(root, image1_path, image2_path, button_size, 4, 0, 3, 3, "C", 10)
zero_button = ToggleButton(root, image1_path, image2_path, button_size, 4, 1, 3, 3, "0",0)
equal_button = ToggleButton(root, button_equal1, button_equal2, button_size, 4, 2, 3, 3, "=",0)

# Uruchomienie aplikacji
root.mainloop()
