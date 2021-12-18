#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:19:27 2021

@author: clockshield
"""

from tkinter import *
import random
root=Tk()
root.title("lol")
root.geometry("400x400")

random_list = Label(root)
sorted_random_list = Label(root)
label_getNumber = Entry(root)
label_getNumberTwo = Entry(root)
label_getNumber.place(relx = 0.5, rely = 0.2, anchor=CENTER)
label_getNumberTwo.place(relx = 0.5, rely = 0.3, anchor=CENTER)
def functionnoname():
    randomnumbers = random.sample(range(int(label_getNumber.get()), int(label_getNumberTwo.get())), 5)
    random_list["text"] = "Random Numbers are: " + str(randomnumbers)
    randomnumbers.sort()
    sorted_random_list["text"] = "Sorted Random Numbers are: " + str(randomnumbers)
    
btn = Button(root,text="click here to get your random nums",command=functionnoname)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
random_list.place(relx = 0.5, rely = 0.5, anchor=CENTER)
sorted_random_list.place(relx = 0.5, rely = 0.6, anchor=CENTER)
root.mainloop()