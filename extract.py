import os
import shutil

def rename_tmpfiles(source_folder, query, source_type):
    source_subfolder = os.path.join(source_folder, query)
    files = os.listdir(source_subfolder)
    count = 1
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_file_name = source_type + "_" + str(count) + file_extension

        # Get the full paths of the source and destination files
        source_path = os.path.join(source_subfolder, file_name)
        destination_path = os.path.join(source_subfolder, new_file_name)

        # Rename the file
        os.rename(source_path, destination_path)

        count += 1

def move_and_delete_tmp_folder(source_folder, destination_folder, query):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    source_subfolder = os.path.join(source_folder, query)

    shutil.move(source_subfolder, destination_folder)

    # Delete the source folder
    os.rmdir(source_folder)