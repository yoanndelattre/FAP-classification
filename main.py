import sys
import os
import crop_images
import extract
from log import log
sys.path.append('downloaders')
import bing_search
import twitter_suggestion

env_execute = os.environ.get('ENV_EXECUTE')

query = os.environ.get('QUERY_SEARCH')

output_download_folder = "output_download"

bing_tmp_folder = "bing_tmp_folder"
twitter_suggestion_tmp_folder = "twitter_suggestion_tmp_folder"

if env_execute == "PROD":
    limit_browser = 100
else:
    limit_browser = 5

output_resize_folder = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    log("-----Download Bing Image-----")
    bing_search.download(query, limit_browser, bing_tmp_folder)
    extract.rename_tmpfiles(bing_tmp_folder, query, "bing")
    extract.move_and_delete_tmp_folder(bing_tmp_folder, output_download_folder, query)

    log("-----Download Twitter Suggestion-----")
    twitter_suggestion.download(query, twitter_suggestion_tmp_folder)
    extract.rename_tmpfiles(twitter_suggestion_tmp_folder, query, "twitter")
    extract.move_and_delete_tmp_folder(twitter_suggestion_tmp_folder, output_download_folder, query)

    log("-----Crop all images-----")
    crop_images.crop_images(query, output_download_folder, output_resize, img_width, img_height)
else:
    log("query is not set.")