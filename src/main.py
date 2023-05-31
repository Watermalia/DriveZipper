import os
import tkinter
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import customtkinter
import configparser
import pyperclip
from zip import zip
import googledrive
from download import download

config = configparser.ConfigParser()
if(os.path.exists('settings.ini')):
    config.read('settings.ini')
    base_url_id = config['DEFAULT']['base_url_id']
else: # First time setup
    pyperclip.copy('drivezipper-sa@drivezipper.iam.gserviceaccount.com')
    base_url = tkinter.simpledialog.askstring("Setup", "Share the base google drive folder with " + 
                                              "\n'drivezipper-sa@drivezipper.iam.gserviceaccount.com'" + 
                                              "\n(which has been copied to your clipboard)\n and paste " +
                                              "the url of the folder here:")
    base_url_id = base_url.split("/")[-1]
    config['DEFAULT'] = {'base_url_id': base_url_id}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

drive = googledrive.Google_Drive(base_url_id)

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
        self.download_bool = tkinter.BooleanVar(value=True)
        self.zip_bool = tkinter.BooleanVar(value=True)
        self.upload_bool = tkinter.BooleanVar(value=True)
        self.delete_bool = tkinter.BooleanVar(value=True)

        # other variables
        self.folders = drive.getFolders()
        self.foldernames = list(self.folders.keys())
        self.driveFolder = None
        self.zipFormat = tkinter.StringVar(value=".zip")

        # Title Label
        self.title_label = customtkinter.CTkLabel(master=root, text = "DriveZipper", font=("Arial", 24)).place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        # Download Section
        self.download_checkbox = customtkinter.CTkCheckBox(master=root, text="Download", variable=self.download_bool, command=self.download_swap)
        self.download_checkbox.place(relx=0.05, rely=0.1)
        self.download_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Insert Magnet Link>")
        self.download_entry.place(relx=0.25, rely=0.1)
        self.download_dir_button = customtkinter.CTkButton(master=root, text="...", width=75, command=lambda: self.ask_for_dir(self.download_entry), state="disabled")
        self.download_dir_button.place(relx=0.8, rely=0.1)

        # Zipping Section
        self.zip_checkbox = customtkinter.CTkCheckBox(master=root, text="Zip", variable=self.zip_bool, command=self.zip_swap)
        self.zip_checkbox.place(relx=0.05, rely=0.2)
        self.zip_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Filename for Zip>")
        self.zip_entry.place(relx=0.25, rely=0.2)
        self.zip_option = customtkinter.CTkOptionMenu(master=root, values=[".zip", ".7z"], width=75, variable=self.zipFormat)
        self.zip_option.place(relx=0.8, rely=0.2)
        self.zip_option.set(".zip")
        self.zip_dir_button = customtkinter.CTkButton(master=root, text="...", width=75, command=lambda: self.ask_for_dir(self.zip_entry))

        # Uploading Section
        self.upload_checkbox = customtkinter.CTkCheckBox(master=root, text="Upload", variable=self.upload_bool)
        self.upload_checkbox.place(relx=0.05, rely=0.3)
        self.upload_dropdown = customtkinter.CTkOptionMenu(master=root, values=self.foldernames, width=300, variable=self.driveFolder)
        self.upload_dropdown.place(relx=0.25, rely=0.3)
        self.upload_dropdown.set("<Select Google Drive Folder>")

        # Delete After Section
        self.delete_checkbox = customtkinter.CTkCheckBox(master=root, text="Delete Zip File After", variable=self.delete_bool)
        self.delete_checkbox.place(relx=0.05, rely=0.4)

        self.ok_button = customtkinter.CTkButton(master=root, text="OK", command=self.submit)
        self.ok_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        
    def download_swap(self):
        self.download_entry.delete(0, END)
        if self.download_checkbox.get():
            self.download_entry.configure(placeholder_text = "<Insert Magnet Link>")
            self.download_dir_button.configure(state="disabled")
        else:
            self.download_entry.configure(placeholder_text = "<Insert Path to Folder>")
            self.download_dir_button.configure(state="normal")

    def zip_swap(self):
        if self.zip_checkbox.get():
            self.enable_download()
            self.zip_option.place(relx=0.8, rely=0.2)
            self.zip_entry.configure(placeholder_text="<Filename for Zip>")
            self.zip_dir_button.place_forget()
        else:
            self.disable_download()
            self.zip_option.place_forget()
            self.zip_entry.configure(placeholder_text="<Insert Path to File>")
            self.zip_dir_button.place(relx=0.8, rely=0.2)

    def enable_download(self):
        self.download_checkbox.configure(state="normal")
        self.download_entry.place(relx=0.25, rely=0.1)
        self.download_dir_button.place(relx=0.8, rely=0.1)

    def disable_download(self):
        self.download_checkbox.deselect()
        self.download_checkbox.configure(state="disabled")
        self.download_entry.place_forget()
        self.download_dir_button.place_forget()

    def enable_zip(self):
        self.zip_checkbox.configure(state="normal")
        self.zip_entry.place(relx=0.25, rely=0.2)
        self.zip_dir_button.place(relx=0.8, rely=0.2)
    
    def disable_zip(self):
        self.zip_checkbox.deselect()
        self.zip_checkbox.configure(state="disabled")
        self.zip_entry.place_forget()
        self.zip_option.place_forget()
        self.zip_dir_button.place_forget()

    def ask_for_dir(self, entry):
        dir = filedialog.askdirectory()
        entry.delete(0, END)
        entry.insert(0, dir)

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