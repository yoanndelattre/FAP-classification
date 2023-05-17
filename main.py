import sys
import os
import crop_images
import move_and_delete_folder
from log import log
sys.path.append('source')
import bing_image

env_execute = os.environ.get('ENV_EXECUTE')

query = os.environ.get('QUERY_SEARCH')

output_original = "output_original"

bing_tmp_folder = "bing_tmp_folder"

if env_execute == "PROD":
    limit_browser = 100
else:
    limit_browser = 5

output_resize = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    log("-----Download Bing Image-----")
    bing_image.download(query, limit_browser, bing_tmp_folder)
    move_and_delete_folder.move_and_delete_folder(bing_tmp_folder, output_original, query, "bing")
    crop_images.crop_images(query, output_original, output_resize, img_width, img_height)
else:
    log("query is not set.")