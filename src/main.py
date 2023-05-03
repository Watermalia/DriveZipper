import os
import tkinter
from tkinter import *
from tkinter import filedialog
import customtkinter
from zip import zip
from drive import uploadFile, getFolders
from torrent import download

# Set theme for GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Main GUI Stuff
class GUI(object):

    def __init__(self, root):
        self.root = root
        root.geometry("600x600")
        root.title("DriveZipper")

        # Define variables here
        # -------------------------------------------------
        # bools for tickboxes
        download_bool = tkinter.BooleanVar(value=True)
        zip_bool = tkinter.BooleanVar(value=True)
        upload_bool = tkinter.BooleanVar(value=True)
        delete_bool = tkinter.BooleanVar(value=True)

        # other variables
        downloadInput = None
        folders = getFolders()
        foldernames = list(folders.keys())
        driveFolder = None
        zipFormat = tkinter.StringVar(value=".zip")

        # Title Label
        title_lbl = customtkinter.CTkLabel(master=root, text = "DriveZipper", font=("Arial", 24))
        title_lbl.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        # Download Section
        download_checkbox = customtkinter.CTkCheckBox(master=root, text="Download", variable=download_bool)
        download_checkbox.place(relx=0.05, rely=0.1)
        download_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Insert Magnet or Direct-Download Link>", textvariable=downloadInput)
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

        dir_button = customtkinter.CTkButton(master=root, text="...", command=self.ask_for_dir)
        dir_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        ok_button = customtkinter.CTkButton(master=root, text="OK", command=self.submit)
        ok_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def ask_for_dir(self):
        dir = filedialog.askdirectory()

    def submit(self):
        
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

root = customtkinter.CTk()
gui = GUI(root)
root.mainloop()