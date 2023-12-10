import tkinter as tk
from tkinter.filedialog import askopenfile
import os
from FinalProject.wavTools import checkType, checkStereo, checkMetaData, makeWavArray
from FinalProject.graphingTools import plotWaveform, plotSpectogram, plotrt60, combinedPlots
from pydub import AudioSegment


def fetchFile():    #defining button command to open file explorer and then display selected file
    file = askopenfile(mode = 'r')
    if file:
        global file_path
        file_path = file.name   #need file_path for merging graphs
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)
        checkType(file_path)    #converting to wav
        checkStereo(file_path)  #converting to mono
        length = checkMetaData(file_path)    #printing file's data and returns wav length
        lengthSec = length / 1000 #converting from ms to seconds

        fileDisplay.insert(tk.END, f"File length: {lengthSec} seconds") #displaying length in listbox

        wavArray = makeWavArray(file_path) #making array of the file's data
        plotWaveform(length, wavArray)

        #plotSpectogram(file_path)   #plotting spectogram

        rt1, max1 = plotrt60(file_path, 250, "Low Frequency")   #plotting and getting max frequency and RT60 values
        rt2, max2 = plotrt60(file_path, 1000, "Mid Frequency")
        rt3, max3 = plotrt60(file_path, 10000, "High Frequency")

        rt1 = abs(rt1)  #making RT60's positive
        rt2 = abs(rt2)
        rt3 = abs(rt3)

        rtdif = (rt1 + rt2 + rt3) / 3
        rtdif -= 0.5
        fileDisplay.insert(tk.END, f"RT60 Difference: {rtdif:.3f} seconds")

        fileDisplay.insert(tk.END, f"Maximum Frequency: {max(max1, max2, max3):.3f} kHz")

        fileDisplay.insert(tk.END, f"Low Frequency RT60: {rt1:.3f} seconds")    #displaying RT60 in listbox
        fileDisplay.insert(tk.END, f"Mid Frequency RT60: {rt2:.3f} seconds")
        fileDisplay.insert(tk.END, f"High Frequency RT60: {rt3:.3f} seconds")

        file.close()

def mergeGraphs():
    if file_path:
        colors = ['#004bc6', '#c6000a', '#6a00c6']
        combinedPlots(file_path, colors)

def displayStats():
    if file_path:
        audio = AudioSegment.from_file(file_path)
        fileDisplay.insert(tk.END, f"Frame Rate: {audio.frame_rate} Hz")
        fileDisplay.insert(tk.END, f"Channels: {audio.channels}")
        fileDisplay.insert(tk.END, f"Sample Width: {audio.sample_width} bytes")
        fileDisplay.insert(tk.END, f"Frame Width: {audio.frame_width} bytes")

        plotSpectogram(file_path)

#GUI
root = tk.Tk()
root.geometry('569x120')
root.title('Sound Modeler    \m/')
button = tk.Button(root, text='Select File', width = 25, command = fetchFile)   #button to display initial graphs
button.grid(row=0, column = 0)

colors = ['#004bc6', '#c6000a', '#6a00c6']
mergeButton = tk.Button(root, text='Merge Graphs' , width=25, command=mergeGraphs) #button to combine graphs
mergeButton.grid(row=0, column=1)

statsButton = tk.Button(root, text='Display Statistics', width=25, command=displayStats)
statsButton.grid(row=0, column=2)

fileDisplay = tk.Listbox(root, height=5, width= 90) #listbox for stats
fileDisplay.grid(row=1, column = 0, columnspan=3)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=fileDisplay.yview)   #scrollbar for listbox
scrollbar.grid(row=1, column=3, sticky=tk.N + tk.S)
fileDisplay.config(yscrollcommand=scrollbar.set)

root.mainloop()