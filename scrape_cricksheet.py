import os
import time
import requests
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
base_url = "https://cricsheet.org"
downloads_url = f"{base_url}/downloads/"
file_destinations = {
    "odis_csv2.zip": r"D:/guvi_fourth_project/ODI_Match/odis_csv2",
    "t20s_json.zip": r"D:/guvi_fourth_project/T20_Match/t20s_json",
    "tests_json.zip": r"D:/guvi_fourth_project/Test_Match/tests_json"
}

# Ensure directories exist
for path in file_destinations.values():
    os.makedirs(path, exist_ok=True)

# Setting up Selenium with Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # for running in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

print("Launching browser...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(downloads_url)
time.sleep(3)  # wait for page to load

# Scraping links for the required files
print("Scanning page for file links...")
links = driver.find_elements(By.TAG_NAME, "a")
download_links = {}
for link in links:
    href = link.get_attribute("href")
    if href:
        filename = os.path.basename(href)
        if filename in file_destinations:
            download_links[filename] = href

driver.quit()

# Downloading and extracting the files
for filename, url in download_links.items():
    extract_dir = file_destinations[filename]
    zip_path = os.path.join(extract_dir, filename)

    print(f"Downloading: {filename}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Extracting: {filename}")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    os.remove(zip_path)
    print(f"Cleaned up: {filename}")

print("Files downloaded and extracted")


