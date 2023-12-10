import tkinter as tk
from tkinter.filedialog import askopenfile
import os
from FinalProject.wavTools import checkType, checkStereo, checkMetaData, makeWavArray
from FinalProject.graphingTools import plotAll, plotSpectogram
from teset import plotrt60

def fetchFile():    #defining button command to open file explorer and then display selected file
    file = askopenfile(mode = 'r')
    if file:
        file_path = file.name
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)

        checkType(file_path)    #converting to wav
        checkStereo(file_path)  #converting to mono
        length = checkMetaData(file_path)    #printing file's data and returns wav length
        lengthSec = length / 1000 #converting from ms to seconds

        fileDisplay.insert(tk.END, f"File length: {lengthSec} seconds") #displaying length in listbox

        wavArray = makeWavArray(file_path) #making array of the file's data
        plotAll(length, wavArray)

        spectogram = plotSpectogram(file_path)


        low = (20, 200)
        mid = (20, 2000)
        high = (2000, 20000)

        plotrt60(file_path, 250, "Low Frequency")
        plotrt60(file_path, 1000, "Mid Frequency")
        plotrt60(file_path, 10000, "High Frequency")

        file.close()


#GUI implementation
root = tk.Tk()
root.geometry('455x120')
root.title('Sound Modeler')
button = tk.Button(root, text='Select File', width = 40, command = fetchFile)
button.grid(row=0, column = 0)

fileDisplay = tk.Listbox(root, height=5, width= 75)
fileDisplay.grid(row=1, column = 0)

root.mainloop()