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

# Import custom functions
from CustomFunctions import *

# Additional Window class
class AdditionalPopup(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Additional Popup")

        # Get the top left corners x and y coordinates if the root window (master)
        position_x = master.winfo_rootx()
        position_y = master.winfo_rooty()
        
        # Set the size of the window
        # .format(position_x, position_y) sets the position at the root windows top left corner so that they overlap
        self.wm_geometry("600x400+{}+{}".format(position_x, position_y))

        # Add widgets to the pop-up window
        label = CTkLabel(self, text="This is an additional pop-up window.")
        label.pack()
        
        # Moves the window to the top
        self.attributes('-topmost', True)

# Add Information Window
class InsertInformation(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Insert Information')
        
        position_x = master.winfo_rootx()
        position_y = master.winfo_rooty()
        
        self.wm_geometry('600x400+{}+{}'.format(position_x, position_y))
        
        IncorrectInputText = 'Invalid data has been entered. Please make sure \nall options have been filled in'
        
        IncorrectInput = CTkLabel(self, text = '', font = ('Ariel', 18), text_color = 'red')
        IncorrectInput.pack()
        IncorrectInput.place(x = 135, y = 250)  
              
        testbutton = CTkButton(self, text = 'Add Data', font = ('Ariel', 30), command = lambda: AddData())
        testbutton.pack()
        testbutton.place(x = 250, y = 300)
        
        CloseButton = CTkButton(self, text = 'Close', font = ('Ariel', 30), text_color = 'red', command = lambda: DestroyWidget(self))
        CloseButton.pack()
        CloseButton.place(x = 250, y = 350)
        

        
        # Text lables for data inputs
        ShowNameText = CTkLabel(self, text = "Name:")
        ShowNameText.place(x = 30, y = 30)
        
        ShowTypeText = CTkLabel(self, text = "Type:")
        ShowTypeText.place(x = 30, y = 60)
        
        ShowGenreText = CTkLabel(self, text = "Genre:")
        ShowGenreText.place(x = 30, y = 90)
        
        ShowPlatformText = CTkLabel(self, text = "Platform:")
        ShowPlatformText.place(x = 30, y = 120)
        
        ShowWatchedText = CTkLabel(self, text = "Watched Status:")
        ShowWatchedText.place(x = 30, y = 150)
        
        # Input Windows
        Default = 'Please Select an Option'
        
        ShowName = CTkEntry(self)
        ShowName.pack()
        ShowName.place(x = 150, y = 30)
        
        FilmSeries = ['Film', 'Series']
        Type = CTkOptionMenu(self, values = FilmSeries)
        Type.set(Default)
        Type.pack()
        Type.place(x = 150, y = 60)
        
        Genre = CTkOptionMenu(self, values = get_unique_values(Data2, 'Genre'))
        Genre.set(Default)
        Genre.pack()
        Genre.place(x = 150, y = 90)
        
        Platform = CTkOptionMenu(self, values = get_unique_values(Data2, 'Platform'))
        Platform.set(Default)
        Platform.pack()
        Platform.place(x = 150, y = 120)
        
        WatchedOptions = ['Yes', 'No', 'Partly']
        WatchedStatus = CTkOptionMenu(self, values = WatchedOptions)
        WatchedStatus.set(Default)
        WatchedStatus.pack()
        WatchedStatus.place(x = 150, y = 150)
        
        # Moves the window to the top level
        self.attributes('-topmost', True)
        
        # Function to get the input values and add them to the csv file
        def AddData():
            data = [ShowName.get(), Type.get(), Genre.get(), Platform.get(), WatchedStatus.get()]
            
            # Check if the inputted data is valid
            valid = True
            for value in data:
                if value == Default:
                    valid = False
                if value == '':
                    valid = False
            if valid:
                # Add the data to the csv file
                add_data(Data2, data)
                
                # Destroy the popup
                DestroyWidget(self)
            else:
                IncorrectInput.configure(text = IncorrectInputText)

# Setting Initial Datasets
Data = pd.read_csv('Data.csv')
Data2 = pd.read_csv('BaseData.csv')

# Create the first window
root = CTk()
root.title('Example Window')
root.geometry('800x600')
root.geometry('+500+200')
set_appearance_mode('dark')
    
# Function to open a new popup depending on the given name
def open_window(name):
    # Return the class based on the given string
    object = globals()[name]
    # Call the class
    object(root)

# Button to add data
AddDataButton = CTkButton(root, text = 'Add Data', font = ('Ariel', 30), corner_radius = 32, command = lambda: open_window('InsertInformation'))
AddDataButton.pack()
AddDataButton.place(x = 325, y = 150)

# Created text and places it on the screen
Text = CTkLabel(master = root, text = "This text should appear on the screen", font = ('Ariel', 30))
Text.pack()
Text.place(x = 50, y = 50)

# Quit Button
QuitButton = CTkButton(master = root, text = "Quit", font = ('Ariel', 30), text_color = 'red', corner_radius = 32, command = lambda: DestroyWidget(root))
QuitButton.pack()
QuitButton.place(x = 325, y = 350)

# Get a new SCV Files Button
FileButton = CTkButton(master = root, text = "File", font = ('Ariel', 30), corner_radius = 90, command = lambda: GetCSVFile())
FileButton.pack()
FileButton.place(x = 325, y = 450)

# Function to destroy a given widget
def DestroyWidget(widget):
    widget.destroy()

# Function to get user to choose a valid csv file
def GetCSVFile():
    global Data
    
    # Get file input of a certain type from user
    try:
        NewCSV = filedialog.askopenfilename(initialdir = "/", title = "Choose a file", filetypes = [("csv files", ".csv")])
    except:
        print("No file was entered")
    else:
        # Check if the new csv file has the correct format
        if(compare_csv_formats(Data, NewCSV)):
            # Check if new csv file is not empty
            if (NewCSV != ""):
                # Set data as the new csv file
                Data = pd.read_csv(NewCSV)
                print('File has been successfully picked')
            else:
                print("No file was selected")
        else:
            print('CSV file has an invalid format')

# Runs the window
root.mainloop()


# To-Do

# Import custom data into user's csv
# View data in user's custom csv
# Select random show or movie
# Select show or movie from given stats
# Show watch history
# Show user watch history stats
# Show user custom data stats


# Plex or Jellyfin