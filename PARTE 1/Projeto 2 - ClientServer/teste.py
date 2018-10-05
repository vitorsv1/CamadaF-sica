from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk()

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                        filetypes =(("PNG Files", "*.png"),("All Files","*.*")),
                        title = "Choose a file."
                        )
    print (name)
    
    #Using try in case user types in unknown file or closes without choosing a file.
    return name


Title = root.title( "File Opener")
label = ttk.Label(root)
label.pack()

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)
    



root.mainloop()
