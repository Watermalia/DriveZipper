import os
import tkinter
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import customtkinter
import configparser
import pyperclip
from zip import zip
import googledrive
from download import download, is_torrent_done, get_torrent_hash, remove_torrent

config = configparser.ConfigParser()
if(os.path.exists('settings.ini')):
    config.read('settings.ini')
    base_url_id = config['DEFAULT']['base_url_id']
else: # First time setup
    pyperclip.copy('drivezipper-sa@drivezipper.iam.gserviceaccount.com')
    dialog = customtkinter.CTkInputDialog(text="Share the base google drive folder with " + 
                                              "\ndrivezipper-sa@\ndrivezipper.iam.gserviceaccount.com" + 
                                              "\n(which has been copied to your clipboard)\n and paste " +
                                              "the url of the folder here:", title="Setup")
    base_url = dialog.get_input()
    if base_url == "" or None:
        raise ValueError("Please enter valid url")
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
        root.geometry("600x400")
        root.title("DriveZipper")

        # Define variables here
        # -------------------------------------------------
        # bools for tickboxes
        self.download_bool = tkinter.BooleanVar(root, name="download", value=True)
        self.zip_bool = tkinter.BooleanVar(root, name="zip", value=True)
        self.upload_bool = tkinter.BooleanVar(root, name="upload", value=True)
        self.delete_folder_bool = tkinter.BooleanVar(root, name="delete_folder", value=True)
        self.delete_zip_bool = tkinter.BooleanVar(root, name="delete_zip", value=True)
        self.remove_torrent_bool = tkinter.BooleanVar(root, name="remove_torrent", value=True)

        # other variables
        self.folders = drive.getFolders()
        self.foldernames = sorted(list(self.folders.keys()))
        self.driveFolder = None
        self.zipFormat = tkinter.StringVar(value=".zip")

        # Title Label
        self.title_label = customtkinter.CTkLabel(master=root, text = "DriveZipper", font=("Arial", 24)).place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        # Download Section
        self.download_checkbox = customtkinter.CTkCheckBox(master=root, text="Download", variable=self.download_bool, command=self.download_swap)
        self.download_checkbox.place(relx=0.05, rely=0.2)
        self.download_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Insert Magnet Link>")
        self.download_entry.place(relx=0.25, rely=0.2)
        self.download_dir_button = customtkinter.CTkButton(master=root, text="...", width=75, command=lambda: self.ask_for_dir(self.download_entry), state="disabled")
        self.download_dir_button.place(relx=0.8, rely=0.2)

        # Zipping Section
        self.zip_checkbox = customtkinter.CTkCheckBox(master=root, text="Zip", variable=self.zip_bool, command=self.zip_swap)
        self.zip_checkbox.place(relx=0.05, rely=0.35)
        self.zip_entry = customtkinter.CTkEntry(master=root, width=300, placeholder_text="<Filename for Zip>")
        self.zip_entry.place(relx=0.25, rely=0.35)
        self.zip_option = customtkinter.CTkOptionMenu(master=root, values=[".zip", ".7z"], width=75, variable=self.zipFormat)
        self.zip_option.place(relx=0.8, rely=0.35)
        self.zip_option.set(".zip")
        self.zip_dir_button = customtkinter.CTkButton(master=root, text="...", width=75, command=lambda: self.ask_for_dir(self.zip_entry))

        # Uploading Section
        self.upload_checkbox = customtkinter.CTkCheckBox(master=root, text="Upload", variable=self.upload_bool)
        self.upload_checkbox.place(relx=0.05, rely=0.5)
        self.upload_dropdown = customtkinter.CTkOptionMenu(master=root, values=self.foldernames, width=300, variable=self.driveFolder)
        self.upload_dropdown.place(relx=0.25, rely=0.5)
        self.upload_dropdown.set("<Select Google Drive Folder>")
        self.new_folder_button = customtkinter.CTkButton(master=root, text="New", width=30, command=self.new_folder)
        self.new_folder_button.place(relx=0.77, rely=0.5)
        self.refresh_folders_button = customtkinter.CTkButton(master=root, text="↺", width=30, command=self.refresh_folders)
        self.refresh_folders_button.place(relx=0.85, rely=0.5)
        self.delete_folder_button = customtkinter.CTkButton(master=root, text="🗑", width=30, command=self.delete_folder)
        self.delete_folder_button.place(relx=0.91, rely=0.5)

        # Delete After Section
        self.remove_torrent_checkbox = customtkinter.CTkCheckBox(master=root, text="Remove Torrent", variable=self.remove_torrent_bool)
        self.remove_torrent_checkbox.place(relx=0.05, rely=0.75)
        self.delete_checkbox = customtkinter.CTkCheckBox(master=root, text="Delete Torrent Files", variable=self.delete_folder_bool)
        self.delete_checkbox.place(relx=0.05, rely=0.65)
        self.delete_checkbox2 = customtkinter.CTkCheckBox(master=root, text="Delete Zip File After", variable=self.delete_zip_bool)
        self.delete_checkbox2.place(relx=0.6, rely=0.65)

        self.ok_button = customtkinter.CTkButton(master=root, text="OK", command=self.submit)
        self.ok_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        
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
            self.zip_option.place(relx=0.8, rely=0.35)
            self.zip_entry.configure(placeholder_text="<Filename for Zip>")
            self.zip_dir_button.place_forget()
        else:
            self.disable_download()
            self.zip_option.place_forget()
            self.zip_entry.configure(placeholder_text="<Insert Path to File>")
            self.zip_dir_button.place(relx=0.8, rely=0.35)

    def enable_download(self):
        self.download_checkbox.configure(state="normal")
        self.download_entry.place(relx=0.25, rely=0.2)
        self.download_dir_button.place(relx=0.8, rely=0.2)

    def disable_download(self):
        self.download_checkbox.deselect()
        self.download_checkbox.configure(state="disabled")
        self.download_entry.place_forget()
        self.download_dir_button.place_forget()

    def enable_zip(self):
        self.zip_checkbox.configure(state="normal")
        self.zip_entry.place(relx=0.25, rely=0.35)
        self.zip_dir_button.place(relx=0.8, rely=0.35)
    
    def disable_zip(self):
        self.zip_checkbox.deselect()
        self.zip_checkbox.configure(state="disabled")
        self.zip_entry.place_forget()
        self.zip_option.place_forget()
        self.zip_dir_button.place_forget()

    def enable_upload(self):
        self.upload_checkbox.configure(state="normal")
        self.upload_dropdown.configure(state="normal")

    def disable_upload(self):
        self.upload_checkbox.deselect()
        self.upload_checkbox.configure(state="disabled")
        self.upload_dropdown.configure(state="disabled")

    def ask_for_dir(self, entry):
        dir = filedialog.askdirectory()
        entry.delete(0, END)
        entry.insert(0, dir)

    def new_folder(self):
        new_folder_dialog = customtkinter.CTkInputDialog(text="New Folder Name:", title="New Folder")
        new_folder_name = new_folder_dialog.get_input()
        drive.create_folder(new_folder_name)

    def refresh_folders(self):
        self.folders = drive.getFolders()
        self.foldernames = sorted(list(self.folders.keys()))
        self.upload_dropdown.configure(values=self.foldernames)

    def delete_folder(self):
        folder_name = self.upload_dropdown.get()
        drive.delete_folder(folder_name)
        self.upload_dropdown.set("<Select Google Drive Folder>")

    def submit(self):
        
        self.ok_button.place_forget()
        self.progressbar = customtkinter.CTkProgressBar(master=root)
        self.progressbar.set(0)
        self.progressbar.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        self.progresslabel = customtkinter.CTkLabel(master=root, text="STARTING")
        self.progresslabel.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        # First we download
        if root.getvar(name="download"):
            self.progresslabel.configure(text="DOWNLOADING...")
            self.progressbar.set(0.25)
            torrent_info = download(magnet_link=self.download_entry.get())
            while not is_torrent_done():
                root.update()

        # Then we zip
        if root.getvar(name="zip"):
            self.progresslabel.configure(text="COMPRESSING...")
            self.progressbar.set(0.5)
            if root.getvar(name="download"):
                zipped = zip(os.path.join(os.getcwd(), "download", torrent_info.name), self.zip_entry.get(), self.zip_option.get())
            else:
                zipped = zip(self.download_entry.get(), self.zip_entry.get(), self.zip_option.get())
            print("done zipping!")

        # Then we upload!
        if root.getvar(name="upload"):
            self.progresslabel.configure(text="UPLOADING...")
            self.progressbar.set(0.75)
            drive.uploadFile(zipped["name"], self.folders[self.upload_dropdown.get()])

        # Then we delete the specified folders/files
        if root.getvar(name="delete_folder"):
            self.progresslabel.configure(text="DELETING...")
            self.progressbar.set(0.9)
            remove_torrent(True, get_torrent_hash())
        elif root.getvar(name="delete_zip") and root.getvar(name="download"):
            self.progresslabel.configure(text="DELETING...")
            self.progressbar.set(0.9)
            remove_torrent(False, get_torrent_hash())
        if root.getvar(name="remove_torrent"):
            self.progresslabel.configure(text="DELETING...")
            self.progressbar.set(0.9)
            os.remove(zipped)

        self.progressbar.place_forget()
        self.progresslabel.configure(text="DONE")
        self.ok_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

root = customtkinter.CTk()
gui = GUI(root)
root.mainloop()