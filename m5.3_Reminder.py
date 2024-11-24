from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame



t = None

def set():
    global t
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


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_sound()
            t = 0
    window.after(10000, check)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()



window = Tk()
window.title ("Напомню")
Label = Label(text = "Установите напоминание")
Label.pack(pady = 10)
set_button = Button (text = "Установите напоминалку", command=set)
set_button.pack()

window.mainloop()
