import sys
import os
import crop_images
from log import log
sys.path.append('source')
import bing_image

output_browser = "output_browser"
query = os.environ.get('QUERY_SEARCH')
limit = os.environ.get('LIMIT_IMG_DOWNLOAD')

output_resize = "output_resize"
img_width = 1024
img_height = 1024

if query is not None:
    if limit is None :
        limit = 10
    else:
        limit = int(limit)
    log("query ->")
    log(query)
    log("limit ->")
    log(limit)
    bing_image.download(query, limit, output_browser)
    crop_images.crop_images(query, output_browser, output_resize, img_width, img_height)
else:
    log("query is not set.")