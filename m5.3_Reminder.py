from email.policy import default
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame



t_p = None
music = False

def set():
    global t_p
    rem = sd.askstring("Время напоминания", "Установите напоминание в 24 ч. формате ЧЧ:ММ")
    #rem = e.get()
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
            text_napomin = sd.askstring ("текст напоминания", "Напишите о чем напомнить: ")
            Label.config(text=f"Напоминание на {hour_p:02}:{minute_p:02} напоминаю: {text_napomin}")
            Label.config(fg="green")
        except Exception as e:
            mb.showerror("Ошибка", f"Неправильно ввели время.Произошла ошибка {e}" )
    else:
        Label.config(text="Поле не заполнили")
        Label.config("fg = red")

def check():
    global t_p
    if t_p:
        now = time.time()
        if now >= t_p:
            play_sound()
            t_p = 0
    window.after(10000, check)

def play_sound():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.MP3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    Label.config(text="Установите заново напоминание")
    Label.config(font=("Showcard Gothic", 16), fg="blue")


window = Tk()
window.geometry("400x150")
window.title ("Напомню")
window.iconbitmap(default="vosklzn.ico")
Label = Label(text = "Установите напоминание",  font=("Showcard Gothic", 16))
Label.pack(pady = 10)
set_button = Button (text = "Установите напоминалку", command=set)
set_button.pack(pady = 10)


stop_btn = Button(text = "остановить проигрывание музыки", command=stop_music)
stop_btn.pack(pady = 10)
check()

window.mainloop()
