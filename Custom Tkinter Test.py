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
from customtkinter import *

Data = pd.read_csv("Data.csv")

# Create the first window
root = CTk()
root.title("Example Window")
root.geometry("800x600")
root.geometry("+500+200")

# Created text and places it on the screen
Text = CTkLabel(root, text = "This text should appear on the screen", font = "Ariel", fg = "black")
Text.pack()
Text.place(x= 50, y = 50)

# Quit Button
QuitButton = CTkButton(root, text = "Quit", font = ("Ariel", 30), fg = "red", command = lambda: DestroyWidget(root))
QuitButton.pack()
QuitButton.place(x = 325, y = 350)

# Get a new SCV Files Button
FileButton = CTkButton(root, text = "File", font = ("Ariel", 30), fg = "black", command = lambda: GetCSVFile())
FileButton.pack()
FileButton.place(x = 325, y = 450)


def DestroyWidget(widget):
    widget.destroy()

def GetCSVFile():
    
    try:
        NewCSV = filedialog.askopenfilename(initialdir = "/", title = "Choose a file", filetypes = [("csv files", ".csv")])
    except:
        print("No file was entered")
    else:
        if (NewCSV != ""):
            csvFile = NewCSV
            print(csvFile)
            Data = pd.read_csv(NewCSV)
            print(Data.info())
            print(Data.head())
        else:
            print("No file was selected")

# Runs the window
root.mainloop()


# To-Do

# Find database API
# Connect to database API
# Import custom data into user's csv
# View data in user's custom csv
# View data from the API
# Use data from both the custom csv file and API
# Update API data information function
# Select random show or movie
# Select show or movie from given stats
# Show watch history
# Recommend shows from custom csv from previously watched shows and genres
# Recommend shows from API from previously watched shows and genres
# Show user watch history stats
# Show user custom data stats
# Use user stats to recommend new shows
# Add shows into custom csv from API


# Plex or Jellyfin