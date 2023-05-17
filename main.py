import sys
import crop_images
sys.path.append('source')
import bing_image

query = sys.argv[1]
limit = 20
output_browser = "output_browser"

output_resize = "output_resize"
img_width = 1024
img_height = 1024

bing_image.download(query, limit, output_browser)

crop_images.crop_images(query, output_browser, output_resize, img_width, img_height)