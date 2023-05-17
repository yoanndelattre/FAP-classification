import os
import shutil

def move_and_delete_folder(source_folder, destination_folder, query, source_type):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    source_subfolder = os.path.join(source_folder, query)

    shutil.move(source_subfolder, destination_folder)

    # Delete the source folder
    os.rmdir(source_folder)