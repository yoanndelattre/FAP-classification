from PIL import Image
import os

def resize_images(query, input_folder, output_folder, width, height):
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

        # Resize the image
        resized_image = image.resize((width, height))

        # Construct the full path to the output file
        output_path = os.path.join(output_folder, file_name)

        # Save the resized image
        resized_image.save(output_path)

        print(f"Resized {file_name} and saved to {output_path}")