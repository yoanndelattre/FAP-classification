from PIL import Image
import os

def crop_images(query, input_folder, output_folder, width, height):
    input_folder = input_folder + "/" + query
    output_folder = output_folder + "/" + query

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # Construct the full path to the input file
        input_path = os.path.join(input_folder, file_name)

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
        output_path = os.path.join(output_folder, file_name)

        # Save the cropped image
        cropped_image.save(output_path)