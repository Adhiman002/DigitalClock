from tkinter import*
from time import strftime

root=Tk()

root.title("Digital Clock")

def time():
    string=strftime("%I:%M:%S %p")
    l.config(text=string)
    l.after(1000,time)
    
l=Label(root,bg='black',fg='white',font=('ds-digital',22,'bold'))
l.pack(anchor='center')

time()


root.mainloop()