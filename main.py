import sys
import os
import crop_images
from log import log
sys.path.append('source')
import bing_image
import instagram_suggestion

env_execute = os.environ.get('ENV_EXECUTE')

query = os.environ.get('QUERY_SEARCH')

output_original = "output_original"

if env_execute == "PROD":
    limit_browser = 100
    limit_instagram = 10
else:
    limit_browser = 5
    limit_instagram = 2

output_resize = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    log("-----Download Bing Image-----")
    bing_image.download(query, limit_browser, output_original)
    log("-----Download Instagram Suggestion-----")
    instagram_suggestion.download(query, limit_instagram, output_original)
    crop_images.crop_images(query, output_original, output_resize, img_width, img_height)
else:
    log("query is not set.")