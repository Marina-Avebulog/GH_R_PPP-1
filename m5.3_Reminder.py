from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame



t = None
music = False

def set():
    global t
    rem = sd.askstring("Время напоминания", "Установите напоминание в 24 ч. формате ЧЧ:ММ")
    if rem:
        try:
            hour_p = int(rem.split(":")[0])
            minute_p = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour= hour_p, minute=minute_p, second=0)
            print(dt)
            t_p = dt.timestamp()
            print(t_p)
            Label.config(text=f"Напоминание на {hour_p:02}:{minute_p:02}")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}" )


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_sound()
            t = 0
    window.after(10000, check)

def play_sound():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    Label.config(text="Установите заново напоминание")


window = Tk()
window.geometry("400x150")
window.title ("Напомню")
Label = Label(text = "Установите напоминание",  font=("Edwardian Script ITC", 16))
Label.pack(pady = 10)
set_button = Button (text = "Установите напоминалку", command=set)
set_button.pack(pady = 10)


stop_btn = Button(text = "остановить проигрывание музыки", command=stop_music)
stop_btn.pack(pady = 10)
check()

window.mainloop()
