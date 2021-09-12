from tkinter import *
from tkinter import filedialog as fd


def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()


root = Tk()
mainmenu = Menu(root)
root.config(menu = mainmenu)
text = Text(width=50, height=25)
text.grid(columnspan=2)


filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = 'Открыть', command = insert_text)
filemenu.add_command(label = 'Сохранить', command = extract_text)
filemenu.add_separator()
filemenu.add_command(label = 'Выход', command = exit)

mainmenu.add_cascade(label = 'Файл', menu = filemenu)


root.mainloop()