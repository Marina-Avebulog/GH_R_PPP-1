from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def set():
    rem = sd.askstring("Время напоминания", "Установите напоминание в 24 ч. формате ЧЧ:ММ")
    if rem:
        try:
            hour_p = int(rem.split(":")[0])
            minute_p = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour= hour_p, minute=minute_p)
            print(dt)
            t_p = dt.timestamp()
            print(t_p)
        except Exception as e:
            mb.showerror("Ошибка", "Произошла ошибка {e}" )

window = Tk()
window.title ("Напомню")
Label = Label(text = "Установите напоминание")
Label.pack(pady = 10)
set_button = Button (text = "Установите напоминалку", command=set)
set_button.pack()

window.mainloop()
