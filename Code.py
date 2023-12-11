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


#Create the first window
root = tk.Tk()
root.title("Example Window")
root.geometry("800x600")
root.geometry("+500+200")

#Runs the window
root.mainloop()