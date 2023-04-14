from zip import zip
from driveupload import uploadFile
import os
import tkinter as tk
from tkinter import filedialog

filename = "testfile"
format = "zip"

root = tk.Tk()
root.withdraw()
dir = filedialog.askdirectory()

# First we zip
# zipped = zip(dir, filename, format)

# Then we upload!
uploadFile()

# TODO
# Then we delete the zip!
