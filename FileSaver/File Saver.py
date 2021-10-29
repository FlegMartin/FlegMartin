#!/usr/bin/env python3


from tkinter import *
import pyautogui
import time

window = Tk()


# File


# Functions

def myClick():
    inputValuefilename = Tfilename.get("1.0", "end-1c")
    inputValue = T.get("1.0", "end-1c")
    if len(T.get("1.0", END))==1 | len(Tfilename.get("1.0", END))==1:
        windowError = Tk()
        lError = Label(windowError, text="Fill file name and content!", fg="Red", font=26, anchor='center')
        lError.pack()
        windowError.configure(bg='Black')
        windowError.title('Error')
        windowError.geometry("200x60")
        windowError.minsize(200, 60)
        windowError.maxsize(200, 60)

    else:
        f = open(inputValuefilename + ".txt", "a")
        f.write(inputValue)
        Tfilename.delete(1.0, "end")
        T.delete(1.0, "end")


def returnblock(event):
    time.sleep(0.001)
    pyautogui.press('backspace')


# add widgets here

lfilename = Label(window, fg='Green', font='TimesNewRoman', border=0, text="File Name:")
lfilename.place(x=805, y=1)
ltext = Label(window, fg='Green', font='TimesNewRoman', border=0, text="Content(Text):", height=1, width=60)
btn = Button(window, text="Save File", fg='Red', command=myClick)
btn.place(x=920, y=900)
window.title('File Saver')
Tfilename = Text(window, bg="white", fg='Red', height=1.2, width=20, font='TimesNewRoman', border=1)
Tfilename.pack()
ltext.pack()
T = Text(window, bg="White", fg='Red', height=40, width=60, font='TimesNewRoman', border=1)
T.pack()



lfilename.bind('<Return>', returnblock)
window.configure(bg='Black')
window.title('File Saver by Martin')
window.geometry("1920x1080")
window.minsize(1920, 1080)
window.maxsize(1920, 1080)
window.mainloop()
