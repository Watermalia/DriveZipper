import py7zr, shutil, os

# Zip up the given directory with specified name and format
def zip(dir, filename: str, format: str):
    
    # Normalize the path
    dir = os.path.normpath(dir)

    if(format == "7z"):     # Compress using 7z format
        with py7zr.SevenZipFile(f"{filename}.7z", 'w') as archive:
            archive.writeall(f'{dir}', os.path.basename(dir))
            archive.close()
        print("Done!")

    elif(format == "zip"):  # Compress using zip format
        shutil.make_archive(filename, 'zip', os.path.dirname(dir), os.path.basename(dir))
        print("Done!!")