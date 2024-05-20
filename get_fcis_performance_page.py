import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

def get_markedup_page(url):
    #resp = requests.get(url).text
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f"//th[@aria-label='Rend. YTD sortable']"))
    ).click()

    resp=driver.page_source
    parsed_page = BeautifulSoup(resp, "html.parser")
    return parsed_page

url="https://www.portfoliopersonal.com/Cotizaciones/SupermercadoFCI"
tbody=get_markedup_page(url).find("tbody")
print(tbody)
