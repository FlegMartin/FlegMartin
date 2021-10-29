from tkinter import *
import pyautogui
import time





window=Tk()

#File





#Functions

def myClick():
    inputValuefilename = Tfilename.get("1.0", "end-1c")
    inputValue = T.get("1.0", "end-1c")
    f = open(inputValuefilename+".txt", "a")
    f.write(inputValue)

def returnblock(event):
    time.sleep(0.001)
    pyautogui.press('backspace')



# add widgets here

lfilename=Label(window, fg='Green', font='TimesNewRoman', border=0, text="File Name:")
lfilename.place(x=132, y=1)
ltext=Label(window, fg='Green', font='TimesNewRoman', border=0, text="Content(Text):")
btn=Button(window, text="Save File", fg='Red', command=myClick)
btn.place(x=260, y=760)
window.title('File Saver')
Tfilename = Text(window, bg="white", fg='Red', height=1.2, width=20, font='TimesNewRoman', border=1)
Tfilename.pack()
ltext.pack()
T = Text(window, bg="White", fg='Red', height=40, width=60, font='TimesNewRoman', border=1)
T.pack()


window.bind('<Return>', returnblock)
window.configure(bg='Black')
window.title('File Saver by Martin')
window.geometry("600x800")
window.mainloop()