from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

def download(subject, num_images, output_dir):
    output_dir = os.path.join(output_dir, subject)
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Configure Chrome options for headless browsing
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    # Specify the path to the Chrome WebDriver executable
    webdriver_path = './chromedriver'

    # Create a Service object
    service = Service(webdriver_path)

    # Create a new instance of the Chrome WebDriver with headless options
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f'https://www.pinterest.com/search/pins/?q={subject}')
    time.sleep(2)

    def scroll_down():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    scroll_down()
    image_elements = driver.find_elements(By.XPATH, "//a/div/div/div/div/div[1]/img")[:num_images]

    count = 0
    for image_element in image_elements:
        try:
            image_url = image_element.get_attribute('src')
            filename = f'{subject}_{count}.jpg'
            save_path = os.path.join(output_dir, filename)
            urllib.request.urlretrieve(image_url, save_path)
            count += 1
            
            if count == num_images:
                break
        except:
            continue

    driver.quit()