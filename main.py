import sys
import resize_images
sys.path.append('source')
import bing_image

query = sys.argv[1]
limit = 5
output_browser = "output_browser"

output_resize = "output_resize"
img_width = 512
img_height = 512

bing_image.download(query, limit, output_browser)

resize_images.resize_images(query, output_browser, output_resize, img_width, img_height)