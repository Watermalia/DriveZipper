import py7zr, shutil, os

# Zip up the given directory with specified name and format
def zip(dir, filename: str, format: str):
    
    # Normalize the path
    dir = os.path.normpath(dir)

    if(format == ".7z"):     # Compress using 7z format
        with py7zr.SevenZipFile(f"{filename}.7z", 'w') as archive:
            archive.writeall(f'{dir}', os.path.basename(dir))
            archive.close()
            return os.path.join(os.getcwd(), f"{filename}.7z")

    elif(format == ".zip"):  # Compress using zip format
        shutil.make_archive(filename, 'zip', os.path.dirname(dir), os.path.basename(dir))
        return os.path.join(os.getcwd(), f"{filename}.zip")