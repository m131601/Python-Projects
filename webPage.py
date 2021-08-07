# Python Ver:   3.9
#
# Author:       Melbae Abernathy
#
# Purpose:      WebPage Generator - Created a Gui with Tkinter that will open an HTML web page.
#               
#
# Tested OS:  This code was written and tested to work with Windows 10.


import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
Inp_user = simpledialog.askstring(title="HTML",
                                  prompt="What's your Name?:")


print("Hello", Inp_user)

def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        

def cancel(self):
        self.master.destroy()

    
# create an html file

import webbrowser

f = open('sale.html','a')

message = """<html>
<body><h1>Stay tuned for our amazing summer sale!</h1></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('sale.html')







if __name__ == "__main__":
    ROOT.withdraw()
