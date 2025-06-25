import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title('Slider Demo')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Slider huidige waarde
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

# Label voor de slider

slider_label = ttk.Label(root, text= 'slider :')
slider_label.grid(column=0,row=0, sticky='w')

slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current_value
)

slider.grid(column=1, row=0, sticky='we')

#label voor de huidige waarde
current_value_label = ttk.Label(root, text='Huidige waarde : ')

# label waarde

value_label = ttk.Label(root, text=get_current_value())

value_label.grid(row=2, columnspan=2, sticky='n')

root.mainloop()