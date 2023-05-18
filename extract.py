import os
import shutil
from log import log

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
        msg_log = destination_path + " is now renamed"
        log(msg_log)


def move_and_delete_tmp_folder(source_folder, destination_folder, query):
    source_subfolder = os.path.join(source_folder, query)
    destination_subfolder = os.path.join(destination_folder, query)

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_subfolder, exist_ok=True)

    # Get the list of files in the source folder
    files = os.listdir(source_subfolder)

    for file in files:
        source_path = os.path.join(source_subfolder, file)
        destination_path = os.path.join(destination_subfolder, file)
        shutil.move(source_path, destination_path)

    # Delete the source folder
    shutil.rmtree(source_folder)
    msg_log = "Data has been moved -> " + destination_folder
    log(msg_log)