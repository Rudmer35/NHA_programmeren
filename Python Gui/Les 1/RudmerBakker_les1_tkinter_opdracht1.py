import tkinter as tk

root =tk.Tk()

root.geometry('1024x768')

root.title('Ik leer Python GUI maken bij NHA')

root.config(bg='red')

left_frame = tk.Frame(root, bg = 'white', width=300, height=300)
left_frame.pack(side="left", expand=True)

right_frame = tk.Frame(root, bg='blue', width=300, height=300)
right_frame.pack(side="right", expand=True)

root.mainloop()
