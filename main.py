import sys
import os
sys.path.append('source')
import bing_image

query = sys.argv[1]
limit = 5
output_dir = "output_original"

if not os.path.exists(output_dir):
        os.makedirs(output_dir)

bing_image.download(query, limit, output_dir)