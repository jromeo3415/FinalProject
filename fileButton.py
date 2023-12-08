import tkinter as tk
from tkinter.filedialog import askopenfile
import os
from checkFileType import checkType
from checkStereo import checkStereo
from checkMetaData import checkMetaData

def fetchFile():    #defining button command to open file explorer and then display selected file
    global file
    file = askopenfile(mode = 'r')
    if file:
        file_path = file.name
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)
        file.close()

        processFile(file_path)

def processFile(file_path):
    converted_file = checkType(file_path)
    is_stereo = checkStereo(converted_file)
    checkMetaData(is_stereo)

root = tk.Tk()
root.geometry('455x50')
root.title('Sound Modeler')
button = tk.Button(root, text='Select File', width = 40, command = fetchFile)
button.grid(row=0, column = 0)

fileDisplay = tk.Listbox(root, height=2, width= 75)
fileDisplay.grid(row=1, column = 0)

#file = checkType(file)  #converting file to .wav

#checkStereo(file)

#checkMetaData(file)

root.mainloop()