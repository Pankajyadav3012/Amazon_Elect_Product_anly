from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import tempfile
import os
import time
import random

#Create a temporary user data directory
user_data_dir = tempfile.mkdtemp()

#Set Chrome options
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

#Set up WebDriver
driver = webdriver.Chrome(options=chrome_options)

#Function to scrape data from a single page
def scrape_page():
    laptops = []
    items = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, "h2").text
        except:
            name = None
        try:
            price = item.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        except:
            price = None
        try:
            rating = driver.execute_script('return arguments[0].querySelector("i.a-icon-star-small span.a-icon-alt")?.textContent', item)
        except:
            rating = None
        try:
            reviews = item.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text
        except:
            reviews = None
        try:
            link = item.find_element(By.CSS_SELECTOR, ".a-link-normal.s-link-style").get_attribute("href")
        except:
            link = None
        try:
            specs = item.find_element(By.CSS_SELECTOR, ".a-text-normal ~ span").text
        except:
            specs = None

        laptops.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating,
            "Number of Reviews": reviews,
            "Specifications": specs,
            "Link": link
        })
    return laptops

#Navigate across all pages
all_laptops = []
base_url = "https://www.amazon.in/s?k=laptop"
page = 1

try:
    while True:
        print(f"Scraping page {page}...")
        driver.get(f"{base_url}&page={page}")
        time.sleep(random.uniform(5, 10))

        #Scrape the first page
        laptops = scrape_page()
        if not laptops:
            print("No more laptops found. Exiting...")
            break
        all_laptops.extend(laptops)
        page += 1

        #Check for Next button to for more pages exist
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".s-pagination-next")
            if not next_button.is_enabled():
                break
        except:
            break

    #Save file to CSV
    if all_laptops:
        df = pd.DataFrame(all_laptops)
        df.to_csv("selenium_laptops_1.csv", index=False)
        print(f"Scraped {len(all_laptops)} laptops. Data saved to 'selenium_laptops_1.csv'.")
    else:
        print("No data found.")
finally:
    driver.quit()