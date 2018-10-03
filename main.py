# -*- coding: utf-8 -*-

import tkinter
import _thread
import time
import numpy

global Password_Entry, string_char_autorised, actived,Button_Start_Stop, Password_Size
file_tmp = open("listCharacter", "r")
string_char_autorised = file_tmp.read().replace("\n","")
file_tmp.close()
actived = True

def password_main():
    global Password_Entry, string_char_autorised, actived
    while True:
        try:
            if actived:
                string_tmp = ""
                for tmp in numpy.random.randint(len(string_char_autorised), size=int(Password_Size.get())):
                    string_tmp += string_char_autorised[tmp]
                Password_Entry.delete(0, len(Password_Entry.get()))
                Password_Entry.insert(0,string_tmp)
                Password_Entry.pack()
            time.sleep(0.07)
        except:
            pass

def start_stop():
    global Password_Entry, string_char_autorised, actived,Button_Start_Stop
    if actived:
        actived = False
    else:
        actived = True


Gui = tkinter.Tk()
Gui.title("Password Generator (Zpass)")
Gui.geometry("300x75")
Gui.resizable(width=False, height=False)
Password_Entry = tkinter.Entry(Gui, width=50)
Password_Entry.insert(0,"test")
Password_Entry.pack()
Button_Start_Stop = tkinter.Button(Gui, text="Stop/Start", command=start_stop)
Button_Start_Stop.pack()
Password_Size = tkinter.Spinbox(Gui, from_=1, to=100)
Password_Size.delete(0, 1)
Password_Size.insert(0, "25")
Password_Size.pack()
_thread.start_new_thread(password_main,())
Gui.mainloop()