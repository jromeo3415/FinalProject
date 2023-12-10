import tkinter as tk
from tkinter.filedialog import askopenfile
import os
from FinalProject.wavTools import checkType, checkStereo, checkMetaData, makeWavArray
from FinalProject.graphingTools import plotWaveform, plotSpectogram, plotrt60, combinedPlots



def fetchFile():    #defining button command to open file explorer and then display selected file
    file = askopenfile(mode = 'r')
    if file:
        global file_path
        file_path = file.name
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)

        checkType(file_path)    #converting to wav
        checkStereo(file_path)  #converting to mono
        length = checkMetaData(file_path)    #printing file's data and returns wav length
        lengthSec = length / 1000 #converting from ms to seconds

        fileDisplay.insert(tk.END, f"File length: {lengthSec} seconds") #displaying length in listbox

        wavArray = makeWavArray(file_path) #making array of the file's data
        plotWaveform(length, wavArray)

        plotSpectogram(file_path)

        rt1, max1 = plotrt60(file_path, 250, "Low Frequency")
        rt2, max2 = plotrt60(file_path, 1000, "Mid Frequency")
        rt3, max3 = plotrt60(file_path, 10000, "High Frequency")

        fileDisplay.insert(tk.END, f"Low Frequency RT60: {rt1}")
        fileDisplay.insert(tk.END, f"Mid Frequency RT60: {rt2}")
        fileDisplay.insert(tk.END, f"High Frequency RT60: {rt3}")

        combinedPlots(file_path, colors)
        file.close()


#GUI
root = tk.Tk()
root.geometry('455x120')
root.title('Sound Modeler')
button = tk.Button(root, text='Select File', width = 25, command = fetchFile)
button.grid(row=0, column = 0)

colors = ['#004bc6', '#c6000a', '#6a00c6']
mergeButton = tk.Button(root, text='Merge Graphs', width=25)
mergeButton.grid(row=0, column=1)

fileDisplay = tk.Listbox(root, height=5, width= 75)
fileDisplay.grid(row=1, column = 0, columnspan=2)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=fileDisplay.yview)
scrollbar.grid(row=1, column=2, sticky=tk.N + tk.S)
fileDisplay.config(yscrollcommand=scrollbar.set)

root.mainloop()