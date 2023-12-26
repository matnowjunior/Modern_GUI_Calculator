from tkinter import *
import tkinter as tk
from tkinter import font
from ctypes import windll
import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
from PIL import Image, ImageTk
import ctypes
# Globalny słownik dla przechowywania obrazów
loaded_images = {}

class ToggleButton:
    def __init__(self, master, image1, image2, image3, size,  row, column, padx=0, pady=0, text="", chosenButton = 0):
        self.size = size
        self.chosenButton = chosenButton
        self.master = master
        self.image1 = self.load_image(image1, size)
        self.image2 = self.load_image(image2, size)
        self.image3 = self.load_image(image3, size)
        self.button = tk.Canvas(master, width=size[0], height=size[1], bg='#261717', bd=0, highlightthickness=0)
        self.image_on_canvas = self.button.create_image(0, 0, anchor=tk.NW, image=self.image1)
        self.button.grid(row=row, column=column, padx=padx, pady=pady)
        self.button.bind('<Button-1>', self.on_click)  
        self.button.bind('<ButtonRelease-1>', self.on_release)
        self.button.bind('<Enter>', self.on_enter)
        self.button.bind('<Leave>', self.on_leave)       
        self.button.create_text(size[0]//2, size[1]//2, text=text, fill="#EBE9E9", font=("Segoe UI", 20))
        
    def button_click(self, number=0):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current)+str(number))

    def load_image(self, path, size):
        if path not in loaded_images:
            loaded_images[path] = ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))
        return loaded_images[path]

    def on_click(self,event):
        global f_num
        global math

        if self.chosenButton == 10:
            e.delete(0, END)
            self.button.itemconfig(self.image_on_canvas, image=self.image2)
        elif self.chosenButton == 11:
            value = 0
            if math == "root":
                e.delete(0, END)
                if value >= 0:
                    value = f_num ** 0.5
                    if value.is_integer():
                        e.insert(0, int(value))
                    else:
                        e.insert(0, value)
                else:
                    e.delete(0, END)
                    e.insert(0, "Error")
            else:
                value = 0
                second_number = float(e.get())
                e.delete(0, END)
                if math == "add":
                    value = f_num + second_number
                elif math == "subtract":
                    value = f_num - second_number
                elif math == "multiply":
                    value = f_num * second_number
                elif math == "divide":
                    value = f_num / second_number
                
                if value.is_integer():
                    e.insert(0, int(value))
                else:
                    e.insert(0, value)
            
        elif self.chosenButton == 12:
            math="add"
            f_num = float(e.get())
            e.delete(0, END)
        elif self.chosenButton == 13:
            math="subtract"
            f_num = float(e.get())
            e.delete(0, END)
        elif self.chosenButton == 14:
            math="multiply"
            f_num = float(e.get())
            e.delete(0, END)
        elif self.chosenButton == 15 :
            math="divide"
            f_num = float(e.get())
            e.delete(0, END)
        elif self.chosenButton == 16 and "." not in e.get():
            current = e.get()
            if current == "":
                current = "0"
            e.delete(0, END)
            e.insert(0, str(current)+str("."))
        elif self.chosenButton == 17:
            if "-" in e.get():
                current = e.get()
                e.delete(0, END)
                e.insert(0, str(current).replace("-", ""))
            else:
                current = e.get()
                e.delete(0, END)
                e.insert(0, str("-")+str(current))
        elif self.chosenButton == 18:
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current)[:-1])
        elif self.chosenButton == 19:
            math="root"
            f_num = float(e.get())
            e.delete(0, END)
        else:
            if self.chosenButton is not 16:
                self.button_click(self.chosenButton)
            self.button.itemconfig(self.image_on_canvas, image=self.image2)    
                

    def on_release(self, event):
        self.button.itemconfig(self.image_on_canvas, image=self.image1)

    def on_enter(self, event):
        self.button.itemconfig(self.image_on_canvas, image=self.image3)

    def on_leave(self, event):
        self.button.itemconfig(self.image_on_canvas, image=self.image1)

#Ustawienei ikony aplikacji w pasku zadań
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.configure(bg='#2B1B1A')
root.title('Kalkulator')
root.geometry('305x450')
root.resizable(False, False)
root.iconbitmap('D:/Python/tkinter/Images/icon.ico')

#Changing title bar color
HWND = windll.user32.GetParent(root.winfo_id())
title_bar_color = 0x1A1B2B
windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))

#Entry widget
large_font = font.Font(family='Segoe UI', size=25)
global e 
e = tk.Entry(root, width=15, bg="#2B1B1A", fg="#EBE9E9", borderwidth=0, font=large_font, insertontime=0)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Ustawienia dla przycisków
button_size = (70, 70)
print(button_size)

image1_path = 'D:/Python/tkinter/Images/button.png'
image2_path = 'D:/Python/tkinter/Images/button3.png'
image3_path = 'D:/Python/tkinter/Images/button2.png'
button_equal1 = 'D:/Python/tkinter/Images/equal_button.png'
button_equal2 = 'D:/Python/tkinter/Images/equal_button2.png'
button_equal3 = 'D:/Python/tkinter/Images/equal_button3.png'
button_backspace1 = 'D:/Python/tkinter/Images/backspace_button1.png'
button_backspace2 = 'D:/Python/tkinter/Images/backspace_button2.png'
button_backspace3 = 'D:/Python/tkinter/Images/backspace_button3.png'
button_root1 = 'D:/Python/tkinter/Images/root_button1.png'
button_root2 = 'D:/Python/tkinter/Images/root_button2.png'
button_root3 = 'D:/Python/tkinter/Images/root_button3.png'

# Tworzenie przycisków
buttons = []
alpha = 1
for row in range(3):
    for column in range(3):
        button = ToggleButton(root, image1_path, image2_path,image3_path, button_size, row+1, column, 3, 3, str(alpha),alpha)
        buttons.append(button)
        alpha += 1

multiply_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size, 1, 3, 3, 3, "x",14)
divide_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size,2, 3, 3, 3, "/",15)
minus_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size,3, 3, 3, 3, "-",13)
plus_button = ToggleButton(root, image1_path,image2_path,image3_path,  button_size, 4, 3, 3, 3, "+",12)
clear_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size,4, 0, 3, 3, "C", 10)
zero_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size,4, 1, 3, 3, "0",0)
equal_button = ToggleButton(root, button_equal1, button_equal2, button_equal3, button_size,5, 3, 3, 3, "=",11)
comma_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size, 4, 2, 3, 3, ".", 16)
logic_button = ToggleButton(root, image1_path,image2_path, image3_path, button_size, 5, 0, 3, 3, "+/-", 17)
backspace_button = ToggleButton(root, button_backspace1,button_backspace2, button_backspace3, button_size, 5, 2, 3, 3, "", 18)
sqrt_button = ToggleButton(root, button_root1, button_root2, button_root3, button_size, 5, 1, 3, 3, "", 19)

# Uruchomienie aplikacji
root.mainloop()
