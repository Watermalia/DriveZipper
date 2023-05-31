import py7zr, shutil, os, zipfile, sys
from py7zr import pack_7zarchive, unpack_7zarchive

# Zip up the given directory with specified name and format
def zip(dir, filename: str, format: str):
    
    # Normalize the path
    dir = os.path.normpath(dir)

    if(format == ".7z"):     # Compress using 7z format
        shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
        shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
        shutil.make_archive(filename, '7zip', os.path.dirname(dir), os.path.basename(dir))
        # with py7zr.SevenZipFile(f"{filename}.7z", 'w') as archive:
        #     archive.writeall(f'{dir}', os.path.basename(dir))
        #     archive.close()
        return {"name": f"{filename}.7z", "dir": os.path.join(os.getcwd(), f"{filename}.7z")}

    elif(format == ".zip"):  # Compress using zip format
        shutil.make_archive(filename, 'zip', os.path.dirname(dir), os.path.basename(dir))
        return {"name": f"{filename}.zip", "dir": os.path.join(os.getcwd(), f"{filename}.zip")}