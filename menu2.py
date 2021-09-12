from tkinter import *

root =Tk()

mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = 'Open')
filemenu.add_command(label = 'New')
filemenu.add_command(label = 'Save')
filemenu.add_command(label = 'Exit')

helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = 'Help')
helpmenu.add_command(label = 'About')

mainmenu.add_cascade(label = 'File', menu = filemenu)
mainmenu.add_cascade(label = 'Help', menu = helpmenu)

root.mainloop()