import sys
import os
import harmonization_images
import extract
import image_classification
from log import log
sys.path.append('downloaders')
import bing_search

env_execute = os.environ.get('ENV_EXECUTE')

query = os.environ.get('QUERY_SEARCH')

name_model_file = "fap_model.h5"
new_name_model_file = "new_fap_model.h5"

output_download_folder = "output_download"

bing_tmp_folder = "bing_tmp_folder"

if env_execute == "PROD":
    limit_browser = 100
else:
    limit_browser = 5

output_crop_folder = "output_crop"
output_resize_folder = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    log("-----Download Bing Image-----")
    bing_search.download(query, limit_browser, bing_tmp_folder)
    extract.rename_tmpfiles(bing_tmp_folder, query, "bing")
    extract.move_and_delete_tmp_folder(bing_tmp_folder, output_download_folder, query)

    log("-----Crop all images-----")
    harmonization_images.crop_images(query, output_download_folder, output_crop_folder, img_width, img_height)

    log("-----Resize all images-----")
    harmonization_images.resize_images(query, output_crop_folder, output_resize_folder, width, height)

    log("-----Start image classification-----")
    image_classification.classification(output_resize_folder, img_height, img_width, name_model_file, new_name_model_file)
else:
    log("query is not set.")