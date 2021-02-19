# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:15:54 2021

@author: Derly garzon
"""

from tkinter import *
from tkcalendar import Calendar,DateEntry


root = Tk()

cal = DateEntry(root,width=30,year=2021)

cal.place(x=20, y=18, width=100, height=30)
cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground ='#fff'  )


root.mainloop()