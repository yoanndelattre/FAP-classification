from bing_image_downloader import downloader
import os

def download(query, limit, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloader.download(
        query,
        limit=limit,
        output_dir=output_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=30,
        verbose=True
    )