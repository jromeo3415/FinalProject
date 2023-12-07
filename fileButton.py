import tkinter as tk
from tkinter.filedialog import askopenfile
import os

def fetchFile():    #defining button command to open file explorer and then display selected file
    file = askopenfile(mode = 'r')
    if file:
        file_path = file.name
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)
        file.close()

root = tk.Tk()
root.geometry('455x50')
root.title('Sound Modeler')
button = tk.Button(root, text='Select File', width = 40, command = fetchFile)
button.grid(row=0, column = 0)

fileDisplay = tk.Listbox(root, height=2, width= 75)
fileDisplay.grid(row=1, column = 0)
root.mainloop()