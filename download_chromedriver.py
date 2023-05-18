import requests
import wget
import zipfile
import os
from log import log

def get():
    webdriver_path = './chromedriver'

    if not os.path.exists(webdriver_path):
        # get the latest chrome driver version number
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text

        msg_log = "The latest chrome stable version is " + version_number
        log(msg_log)

        # build the donwload url
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_linux64.zip"

        # download the zip file using the url built above
        latest_driver_zip = wget.download(download_url,'chromedriver.zip')

        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall() # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(latest_driver_zip)

    else:
        log("webdriver already exists.")