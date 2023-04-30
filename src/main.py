import os
import tkinter
from tkinter import *
from tkinter import filedialog
import customtkinter
from zip import zip
from drive import uploadFile, getFolders
from torrent import download

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Define variables here
download_bool = tkinter.BooleanVar(value=True)
download_input = tkinter.StringVar()
zip_bool = tkinter.BooleanVar(value=True)
upload_bool = tkinter.BooleanVar(value=True)
delete_bool = tkinter.BooleanVar(value=True)
folders = getFolders()
foldernames = list(folders.keys())
driveFolder = tkinter.StringVar()
zipFormat = tkinter.StringVar(value=".zip")

def ask_for_dir():
    dir = filedialog.askdirectory()

def update_download_label():
    if download_bool:
        download_entry._placeholder_text = "<Insert Magnet Link>"
    else:
        download_entry._placeholder_text = "<Insert Folder Path>"

def submit():
    
    # First we torrent
    #torrent = download()

    # Then we zip
    #zipped = zip(dir, filename, format)

    # Then we upload!
    #uploadFile()

    # TODO
    # Then we delete the zip!
    #os.remove(zipped)
    pass

# Main GUI Stuff
root = customtkinter.CTk()
root.geometry("600x600")
root.title("DriveZipper")



# Download Section
download_checkbox = customtkinter.CTkCheckBox(master=root, text="Download", variable=download_bool, command=update_download_label)
download_checkbox.place(relx=0.05, rely=0.1)
download_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Insert Magnet Link>", textvariable=download_input)
download_entry.place(relx=0.25, rely=0.1)

# Zipping Section
zip_checkbox = customtkinter.CTkCheckBox(master=root, text="Zip", variable=zip_bool)
zip_checkbox.place(relx=0.05, rely=0.2)
zip_name = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Filename for Zip>")
zip_name.place(relx=0.25, rely=0.2)
zip_format = customtkinter.CTkOptionMenu(master=root, values=[".zip", ".7z"], width=75, variable=zipFormat)
zip_format.place(relx=0.8, rely=0.2)
zip_format.set(".zip")

# Uploading Section
upload_checkbox = customtkinter.CTkCheckBox(master=root, text="Upload", variable=upload_bool)
upload_checkbox.place(relx=0.05, rely=0.3)
upload_dropdown = customtkinter.CTkOptionMenu(master=root, values=foldernames, width=300, variable=driveFolder)
upload_dropdown.place(relx=0.25, rely=0.3)
upload_dropdown.set("<Select Google Drive Folder>")

# Delete After Section
delete_checkbox = customtkinter.CTkCheckBox(master=root, text="Delete After", variable=delete_bool)
delete_checkbox.place(relx=0.05, rely=0.4)

dir_button = customtkinter.CTkButton(master=root, text="...", command=ask_for_dir)
dir_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

ok_button = customtkinter.CTkButton(master=root, text="OK", command=submit)
ok_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

root.mainloop()