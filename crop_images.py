from PIL import Image
import os
from log import log
import shutil

def crop_images(query, input_folder, output_folder, width, height):
    input_subfolder = os.path.join(input_folder, query)
    output_subfolder = os.path.join(output_folder, query)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_subfolder):
        os.makedirs(output_subfolder)

    # Get the list of files in the input folder
    files = os.listdir(input_subfolder)

    for file_name in files:
        # Construct the full path to the input file
        input_path = os.path.join(input_subfolder, file_name)

        # Open the image using PIL
        image = Image.open(input_path)

        # Get the current dimensions of the image
        current_width, current_height = image.size

        # Calculate the center coordinates for cropping
        left = (current_width - width) / 2
        top = (current_height - height) / 2
        right = (current_width + width) / 2
        bottom = (current_height + height) / 2

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Construct the full path to the output file
        output_path = os.path.join(output_subfolder, file_name)

        # Save the cropped image
        cropped_image.save(output_path)

        msg_log = output_path + " is now cropped"
        log(msg_log)

    # Delete the source folder
    shutil.rmtree(input_folder)
    msg_log = "Data has been moved -> " + output_folder
    log(msg_log)