import tkinter as tk
import fetchFile

root = tk.Tk()
root.geometry(100, 100)
root.title('Sound Modeler')
button = tk.button(root, text='Select File', width = 15, command = fetchFile)