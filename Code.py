import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import Listbox
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
        label = CTkLabel(self, text = "This is an additional pop-up window.")
        label.pack()
        
        # Moves the window to the top
        self.attributes('-topmost', True)

# Choose a random film or series window
class ChooseShow(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Show Selection')

        position_x = master.winfo_rootx()
        position_y = master.winfo_rooty()
        
        self.wm_geometry("600x500+{}+{}".format(position_x, position_y))

        # Title Lablel
        label = CTkLabel(self, text = "Choose a random show", font = ('Ariel', 30))
        label.pack()
        label.place(x = 150, y = 20)
        
        # Text lables for data inputs
        ShowTypeText = CTkLabel(self, text = "Type:", font = ('Ariel', 25, 'bold'))
        ShowTypeText.place(x = 30, y = 70)
        
        ShowGenreText = CTkLabel(self, text = "Genre:", font = ('Ariel', 25, 'bold'))
        ShowGenreText.place(x = 30, y = 120)
        
        ShowPlatformText = CTkLabel(self, text = "Platform:", font = ('Ariel', 25, 'bold'))
        ShowPlatformText.place(x = 30, y = 170)
        
        ShowWatchedText = CTkLabel(self, text = "Watched:", font = ('Ariel', 25, 'bold'))
        ShowWatchedText.place(x = 30, y = 220)

        # Input Windows
        Default = 'Please Select an Option'
        
        FilmSeries = ['Film', 'Series']
        Type = CTkOptionMenu(self, values = FilmSeries, font = ('Ariel', 25))
        Type.set(Default)
        Type.pack()
        Type.place(x = 150, y = 70)
        
        Genre = CTkOptionMenu(self, values = get_unique_values(Data, 'Genre'), font = ('Ariel', 25))
        Genre.set(Default)
        Genre.pack()
        Genre.place(x = 150, y = 120)
        
        Platform = CTkOptionMenu(self, values = get_unique_values(Data, 'Platform'), font = ('Ariel', 25))
        Platform.set(Default)
        Platform.pack()
        Platform.place(x = 150, y = 170)
        
        WatchedOptions = ['Yes', 'No', 'Partly']
        WatchedStatus = CTkOptionMenu(self, values = WatchedOptions, font = ('Ariel', 25))
        WatchedStatus.set(Default)
        WatchedStatus.pack()
        WatchedStatus.place(x = 150, y = 220)

        # Switches to Toggle Variables
        FilmSeriesSwitch = CTkSwitch(self, text = 'Use', font = ('Ariel', 25, 'bold'), height = 40, width = 40)
        FilmSeriesSwitch.pack()
        FilmSeriesSwitch.place(x = 485, y = 60)

        GenreSwitch = CTkSwitch(self, text = 'Use', font = ('Ariel', 25, 'bold'), height = 40, width = 40)
        GenreSwitch.pack()
        GenreSwitch.place(x = 485, y = 110)

        PlatformSwitch = CTkSwitch(self, text = 'Use', font = ('Ariel', 25, 'bold'), height = 40, width = 40)
        PlatformSwitch.pack()
        PlatformSwitch.place(x = 485, y = 160)

        WatchedStatusSwitch = CTkSwitch(self, text = 'Use', font = ('Ariel', 25, 'bold'), height = 40, width = 40)
        WatchedStatusSwitch.pack()
        WatchedStatusSwitch.place(x = 485, y = 210)

        # Function to get the switch and input values
        def ChooseShow():
            # Get the switch values
            film_series = FilmSeriesSwitch.get()
            genre = GenreSwitch.get()
            platform = PlatformSwitch.get()
            watched_status = WatchedStatusSwitch.get()

            # Get the input values if the switch is True
            if film_series:
                film_series_value = Type.get()
            else:
                film_series_value = None

            if genre:
                genre_value = Genre.get()
            else:
                genre_value = None

            if platform:
                platform_value = Platform.get()
            else:
                platform_value = None

            if watched_status:
                watched_status_value = WatchedStatus.get()
            else:
                watched_status_value = None
                
            # Get the random show
            result = choose_random_show(Data, Type = film_series_value, Genre = genre_value, Platform = platform_value, Watched = watched_status_value)
            
            # Check if the result is a single string
            if isinstance(result, str):
                clear_labels()
            else:
                # Display the result on the screen
                update_result_labels(result, result_labels)
        
        # Create labels to display the result data
        result_labels = []
        
        # Functiont to clear labels
        def clear_labels():
            for label in result_labels:
                label.destroy()
        
        # Function to update the labels with the result data
        def update_result_labels(result, result_labels):
            
            # Clear existing labels
            clear_labels()
                
            # Get the column names and values from the result dataframe
            columns = result.index
            values = result.values
            
            # Create and place labels for each column and value
            for i in range(len(columns)):
                label_text = f"{columns[i]}: {values[i]}"
                label = CTkLabel(self, text = label_text, font = ('Ariel', 18))
                label.pack()
                label.place(x = 250, y = 350 + i * 30)
                
                # Add the label to the result_labels list
                result_labels.append(label)
        
        
        # Button to choose a random show
        ChooseButton = CTkButton(self, text = 'Choose Show', font = ('Ariel', 30), width = 100, command = lambda: ChooseShow())
        ChooseButton.pack()
        ChooseButton.place(x = 200, y = 300)
        
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
              
        AddDataButton = CTkButton(self, text = 'Add Data', font = ('Ariel', 30), width = 100, command = lambda: AddData())
        AddDataButton.pack()
        AddDataButton.place(x = 100, y = 300)
        
        CloseButton = CTkButton(self, text = 'Cancel', font = ('Ariel', 30), width = 100, text_color = 'red', command = lambda: DestroyWidget(self))
        CloseButton.pack()  
        CloseButton.place(x = 400, y = 300)
        
        
        # Text lables for data inputs
        
        ShowNameText = CTkLabel(self, text = "Name:", font = ('Ariel', 25))
        ShowNameText.place(x = 30, y = 30)
        
        ShowTypeText = CTkLabel(self, text = "Type:", font = ('Ariel', 25))
        ShowTypeText.place(x = 30, y = 60)
        
        ShowGenreText = CTkLabel(self, text = "Genre:", font = ('Ariel', 25))
        ShowGenreText.place(x = 30, y = 90)
        
        ShowPlatformText = CTkLabel(self, text = "Platform:", font = ('Ariel', 25))
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
        
        Genre = CTkOptionMenu(self, values = get_unique_values(Data, 'Genre'))
        Genre.set(Default)
        Genre.pack()
        Genre.place(x = 150, y = 90)
        
        Platform = CTkOptionMenu(self, values = get_unique_values(Data, 'Platform'))
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
            dataInput = [ShowName.get(), Type.get(), Genre.get(), Platform.get(), WatchedStatus.get()]
            
            # Check if the inputted data is valid
            valid = True
            for value in dataInput:
                if value == Default:
                    valid = False
                if value == '':
                    valid = False
            if valid:
                # Add the data to the csv file
                add_data(Data, dataInput)
                
                # Destroy the popup
                DestroyWidget(self)
            else:
                IncorrectInput.configure(text = IncorrectInputText)

# Test Popup Window
class EditDataPopup(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Edit Data")

        # Get the top left corners x and y coordinates if the root window (master)
        position_x = master.winfo_rootx()
        position_y = master.winfo_rooty()

        # Set the size of the window
        # .format(position_x, position_y) sets the position at the root windows top left corner so that they overlap
        self.wm_geometry("700x450+{}+{}".format(position_x, position_y))

        # Declare Data as a global variable
        global Data

        scrollbar = CTkScrollbar(self)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        listbox = tk.Listbox(self, yscrollcommand = scrollbar.set, width = 25, height = 50)
        listbox.pack(side = tk.LEFT, fill = tk.BOTH)

        self.text = CTkLabel(self, width = 25, height = 50, font=('Ariel', 30), text='')
        self.text.pack(side = tk.TOP, fill = tk.BOTH)

        for index, row in Data.iterrows():
            listbox.insert(tk.END, row['Name'])

        def show_details(event):
            selected_index = listbox.curselection()
            selected_row = Data.iloc[selected_index]
            self.text.configure(
                text=f"Name: {selected_row['Name']}\nType: {selected_row['Type']}\nGenre: {selected_row['Genre']}\nPlatform: {selected_row['Platform']}\nWatched Status: {selected_row['Watched']}")

        def update_data():
            selected_index = listbox.curselection()
            selected_row = Data.iloc[selected_index]
            # Update the selected row with the new data
            selected_row['Name'] = self.entries[0].get() or selected_row['Name']
            selected_row['Type'] = self.entries[1].get() or selected_row['Type']
            selected_row['Genre'] = self.entries[2].get() or selected_row['Genre']
            selected_row['Platform'] = self.entries[3].get() or selected_row['Platform']
            selected_row['Watched'] = self.entries[4].get() or selected_row['Watched']

            # Save the updated data to the csv file
            Data.iloc[selected_index] = selected_row
            Data.to_csv(Data_csv, index = False)

        def delete_data():
            selected_index = int(listbox.curselection()[0])
            
            if selected_index is not None:
                Data.drop(Data.index[selected_index], inplace=True)
                Data.to_csv(Data_csv, index = False)
                listbox.delete(selected_index)

        update_button = CTkButton(self, font = ('Ariel', 30), corner_radius = 90, text = 'Update', command = update_data)
        update_button.pack(side = tk.TOP)

        delete_button = CTkButton(self, font = ('Ariel', 30), corner_radius = 90, text = 'Delete', command = delete_data)
        delete_button.pack(side = tk.TOP)
        
        BackButton = CTkButton(self, text = 'Back', font = ('Ariel', 30), text_color = 'red', corner_radius = 90, command = lambda: DestroyWidget(self))
        BackButton.pack()
        BackButton.place(x = 550, y = 355)

        # Input Windows
        self.entries = []
        for i in range(4):
            if i != 2:
                entry = CTkEntry(self)
                entry.pack()
                entry.place(x = 400, y = 280 + i * 30)
                self.entries.append(entry)

        TypeOptions = ['Film', 'Series']
        ShowTypeDropDown = CTkOptionMenu(self, values=TypeOptions)
        ShowTypeDropDown.pack()
        ShowTypeDropDown.place(x = 400, y = 280 + 2 * 30)
        self.entries.append(ShowTypeDropDown)

        WatchedOptions = ['Yes', 'No', 'Partly']
        WatchedStatusDropDown = CTkOptionMenu(self, values=WatchedOptions)
        WatchedStatusDropDown.pack()
        WatchedStatusDropDown.place(x = 400, y = 280 + 4 * 30)
        self.entries.append(WatchedStatusDropDown)
        
        # Input Labels
        ShowNameText = CTkLabel(self, text = "Name:", font = ('Ariel', 25))
        ShowNameText.pack()
        ShowNameText.place(x = 175, y = 280)
        
        ShowTypeText = CTkLabel(self, text = "Type:", font = ('Ariel', 25))
        ShowTypeText.pack()
        ShowTypeText.place(x = 175, y = 310)
        
        ShowGenreText = CTkLabel(self, text = "Genre:", font = ('Ariel', 25))
        ShowGenreText.pack()
        ShowGenreText.place(x = 175, y = 340)
        
        ShowPlatformText = CTkLabel(self, text = "Platform:", font = ('Ariel', 25))
        ShowPlatformText.pack()
        ShowPlatformText.place(x = 175, y = 370)
        
        ShowWatchedText = CTkLabel(self, text = "Watched Status:", font = ('Ariel', 25))
        ShowWatchedText.pack()
        ShowWatchedText.place(x = 175, y = 400)
        
        listbox.pack(side = 'left', fill = 'both')
        scrollbar.configure(command = listbox.yview)
        listbox.bind('<<ListboxSelect>>', show_details)

        # Moves the window to the top
        self.attributes('-topmost', True)

# Setting Initial Datasets
Data = pd.read_csv('BaseData.csv')
Data_csv = 'BaseData.csv'

# Create the first window
root = CTk()
root.title('Main Window')
root.geometry('800x600')
root.geometry('+500+200')
set_appearance_mode('dark')
    
# Function to open a new popup depending on the given name
def open_window(name):
    # Return the class based on the given string
    object = globals()[name]
    # Call the class
    object(root)

# Add Data Button
AddDataButton = CTkButton(root, text = 'Add Data', font = ('Ariel', 30), corner_radius = 32, command = lambda: open_window('InsertInformation'))
AddDataButton.pack()
AddDataButton.place(x = 325, y = 150)

# Created text and places it on the screen
Text = CTkLabel(master = root, text = "Move and Show Manager", font = ('Ariel', 50))
Text.pack()
Text.place(x = 125, y = 50)

# Quit Button
QuitButton = CTkButton(master = root, text = "Quit", font = ('Ariel', 30), text_color = 'red', corner_radius = 32, command = lambda: DestroyWidget(root))
QuitButton.pack()
QuitButton.place(x = 325, y = 350)

# Get a new SCV Files Button
FileButton = CTkButton(master = root, text = "Change CSV File", font = ('Ariel', 30), corner_radius = 90, command = lambda: GetCSVFile())
FileButton.pack()
FileButton.place(x = 270, y = 450)

# Invalid file selected text
InvalidFileTextValue = 'The selected file is not in the correct format.\nPlease reformat the file or choose another'
InvalidFileText = CTkLabel(master = root, text = '', font = ('Ariel', 18), text_color = 'red')
InvalidFileText.pack()
InvalidFileText.place(x = 235, y = 500)

# Choose Show Button
ChooseShowButton = CTkButton(master = root, text = 'Choose Show or Film', font = ('Ariel', 30), corner_radius = 90, command = lambda: open_window('ChooseShow'))
ChooseShowButton.pack()
ChooseShowButton.place(x = 250, y = 275)

# Edit Data Button
EditDataButton = CTkButton(master = root, text = 'Edit Data', font = ('Ariel', 30), corner_radius = 90, command = lambda: open_window('EditDataPopup'))
EditDataButton.pack()
EditDataButton.place(x = 325, y = 200)

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
                Data_csv = NewCSV
                InvalidFileText.config(text = '')
            else:
                print("No file was selected")
        else:
            print('CSV file has an invalid format')
            InvalidFileText.configure(text = InvalidFileTextValue)

# Runs the window
root.mainloop()