from bing_image_downloader import downloader

def download(query, limit, output_dir):
    downloader.download(
        query,
        limit=limit,
        output_dir=output_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True
    )