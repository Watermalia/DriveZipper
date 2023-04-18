import os
import tkinter
from tkinter import *
from tkinter import filedialog
import customtkinter
from zip import zip
from driveupload import uploadFile, getFolders
from torrent import download, login

username = 'admin'
password = ''

filename = "testfile"
format = "zip"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def ask_for_dir():
    dir = filedialog.askdirectory()

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

download_bool = tkinter.BooleanVar(root, True)
zip_bool = tkinter.BooleanVar(root, True)
upload_bool = tkinter.BooleanVar(root, True)
delete_bool = tkinter.BooleanVar(root, True)
folders = getFolders()
foldernames = list(folders.keys())
driveFolder = None

download_checkbox = customtkinter.CTkCheckBox(master=root, text="Download", variable=download_bool)
download_checkbox.place(relx=0.05, rely=0.1)
download_magnet_link = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Insert Magnet Link>")
download_magnet_link.place(relx=0.25, rely=0.1)

zip_checkbox = customtkinter.CTkCheckBox(master=root, text="Zip", variable=zip_bool)
zip_checkbox.place(relx=0.05, rely=0.2)
zip_magnet_link = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Filename for Zip>")
zip_magnet_link.place(relx=0.25, rely=0.2)


upload_checkbox = customtkinter.CTkCheckBox(master=root, text="Upload", variable=upload_bool)
upload_checkbox.place(relx=0.05, rely=0.3)
upload_dropdown = customtkinter.CTkOptionMenu(master=root, values=foldernames, width=300, variable=driveFolder)
upload_dropdown.place(relx=0.25, rely=0.3)
upload_dropdown.set("<Select Google Drive Folder>")

delete_checkbox = customtkinter.CTkCheckBox(master=root, text="Delete After", variable=delete_bool)
delete_checkbox.place(relx=0.05, rely=0.4)

dir_button = customtkinter.CTkButton(master=root, text="...", command=ask_for_dir)
dir_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

ok_button = customtkinter.CTkButton(master=root, text="OK", command=submit)
ok_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

root.mainloop()

# try to login to qbittorrent
#login(username, password)