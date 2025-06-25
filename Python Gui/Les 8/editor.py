from tkinter import *
from tkinter import filedialog
import os

#Root pagina aanmaken voor het gebruik van widgets.
root = Tk()
root.geometry=("860x600")
root.title('Text Editor')
root.resizable(False,False)

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes =[('Text file', '*.txt'),('All files', '*.*')])
    if file is not None:
        text = file.read()
        text_box.insert(END, text)
        file.close()
        
    
#Functie om het tekst bestand op te slaan
def save_file():
    file = filedialog.asksaveasfilename(title= 'Save file',
    filetypes=[('Text file', '*.txt')])

def information():
    info = Toplevel(root)
    info.title('About')
    info.geometry("200x100")
    info.resizable(False,False)

    Label(info, text="Version: 1.0").pack()
    Label(info, text="Date: 21-06-2025").pack()
    Label(info, text="Maker: Rudmer Bakker").pack()
    Button(info, text="Ok", command= info.destroy).pack()



#Titel aanmaken boven de widget waar de tekst getypt kan worden.
Label(root, text="Text Editor").pack()

#Text box maken voor het typen van tekst.
text_box = Text(root, undo=True)
text_box.pack(padx=20, pady=20)

#Menu aanmaken en definieren.
mijn_menu = Menu(root)
root.config(menu=mijn_menu)

#File-menu definieren
file_menu= Menu(mijn_menu, tearoff=False)
mijn_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open file", command= lambda: open_file())
file_menu.add_command(label="Save as..", command= lambda: save_file())
file_menu.add_command(label="Exit", command=root.quit)

#Edit-menu definieren
edit_menu = Menu(mijn_menu, tearoff=False)
mijn_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command= text_box.edit_undo)
edit_menu.add_command(label="Redo", command= text_box.edit_redo)
edit_menu.add_command(label="Clear", command= lambda: text_box.delete('1.0', END))

#Help-menu definieren
help_menu = Menu(mijn_menu, tearoff=False)
mijn_menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About", command= lambda: information())

root.mainloop()