



import shutil
import os
import tkinter as tk

from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()

#set where the source of files are
source = '/Users/melba/OneDrive/Documents/GitHub/Python-Projects/folderA/'

#set the destination path to folderB
destination = '/Users/melba/OneDrive/Documents/GitHub/Python-Projects/folderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

