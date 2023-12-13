import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from enum import Enum
import csv
import os

csvFile = ""

#Create the first window
root = tk.Tk()
root.title("Example Window")
root.geometry("800x600")
root.geometry("+500+200")

#Created text and places it on the screen
Text = tk.Label(root, text = "This text should appear on the screen", font = "Ariel", fg = "black")
Text.pack()
Text.place(x= 50, y = 50)

#Created a button that will appear on the screen
QuitButton = tk.Button(root, text = "Quit", font = ("Ariel", 30), fg = "red", command = lambda: DestroyWidget(root))
QuitButton.pack()
QuitButton.place(x = 325, y = 375)

def DestroyWidget(widget):
    widget.destroy()

def GetCSVFile():
    NewCSV = filedialog.askdirectory()
    if (CheckIfCSV(NewCSV)):
        csvFile = NewCSV
    else:
        print("Incorrect filetype entered")

def CheckIfCSV(File):
    if ():
        return True
    else:
        return False

#Runs the window
root.mainloop()