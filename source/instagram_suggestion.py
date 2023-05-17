import instaloader
import os
import shutil

def move_files_and_delete_folder(source_folder, destination_folder):
    # Move all files from the source folder to the destination folder
    files = os.listdir(source_folder)
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)

    # Delete the source folder
    os.rmdir(source_folder)

def remove_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in extensions:
                os.remove(file_path)

def download(search_query, num_images, output_folder):
    output_folder = output_folder + "/" + search_query
    tmp_folder="tmp"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Search for the given query
    suggestions = loader.get_hashtag_posts(search_query)

    # Iterate over the suggestions and download images
    count = 0
    for suggestion in suggestions:
        if count >= num_images:
            break

        # Download the image
        loader.download_post(suggestion, target=os.path.join(tmp_folder))
        count += 1

    remove_files_with_extensions(tmp_folder, ".json.xz")
    remove_files_with_extensions(tmp_folder, ".txt")

    move_files_and_delete_folder(tmp_folder, output_folder)