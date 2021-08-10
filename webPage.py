# Python Ver:   3.9
#
# Author:       Melbae Abernathy
#
# Purpose:      WebPage Generator - Created a Gui with Tkinter that will open an HTML web page.
#               
#
# Tested OS:  This code was written and tested to work with Windows 10.


import tkinter
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Web Page Generator!')
        self.master.config(bg='lightgray')
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(2, weight = 1)
        self.master.columnconfigure(1, weight = 2)
        self.master.rowconfigure(0, weight = 1)
        self.master.rowconfigure(2, weight = 1)

        self.textbox = Text(master, height =  6, width = 10)
        self.textbox.grid(row = 1, column = 1)

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row = 3, column = 1)
    def submit(self):
        f = open('sale.html','w')

        self.message = """<html>
        <body><h1>Stay tuned for our amazing summer sale!</h1></body>
        </html>"""

        f.write(self.message)
        f.close()

        webbrowser.open_new_tab('sale.html')
        
               

        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    




