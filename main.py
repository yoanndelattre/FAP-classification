import sys
import os
import crop_images
from log import log
sys.path.append('source')
import bing_image
import instagram_suggestion

query = os.environ.get('QUERY_SEARCH')

output_original = "output_original"

limit_browser = 10
limit_instagram = 5

output_resize = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    log("query ->")
    log(query)
    #bing_image.download(query, limit_browser, output_original)
    instagram_suggestion.download(query, limit_instagram, output_original)
    crop_images.crop_images(query, output_original, output_resize, img_width, img_height)
else:
    log("query is not set.")