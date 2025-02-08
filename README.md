# 📦 Amazon Product Scraping & Analysis  

## 🚀 Overview  
This project automates the extraction of Amazon product data (specifically Electronics Product) using Selenium.  This scraped data is then cleaned and analyzed, with visualizations created in Power BI. This provides insights into product pricing, ratings, and specifications, enabling users to make informed decisions.

## 📂 Project Structure  
- **`amazon_scraping_code.py`** – This file is python script for web scraping Amazon product data using Selenium. It extracts essential details such as product names, prices, ratings, reviews, and specifications.
- **`amazon_products1_cleaned.csv`** –  this is cleaned dataset ready for analysis, containing refined and structured data for easy visualization. 
- **`Cleaning_code.ipynb`** – VScode for cleaning and preprocessing the scraped data, handling missing values, and standardizing formats. 
- **`amazon_dash_powerbi_.pbix`** – This is Power BI dashboard for analyzing and visualizing the extracted data, with interactive charts and graphs showcasing trends and insights.

## 🛠️ Tools Used
- **Python** (Selenium, Pandas) for data extraction & processing  
- **VSCODE** for cleaning and transformation  
- **Power BI** for visualization  

## 📜 How to Use  

### 1️⃣ Web Scraping  
Run this script to scrape Amazon electronics product data:

python amazon_scraping_code.py

This will generate a CSV file (selenium_laptops_1.csv) containing extracted data.

### 2⃣ Data Cleaning

Open Cleaning_code.ipynb in Jupyter Notebook/ vscode and follow the steps to clean and preprocess the data, including:

Removing duplicate entries

Handling missing values

Standardizing price and rating formats

### 3⃣ Visualization

Load amazon_dash_powerbi_.pbix into Power BI to explore interactive insights, including:

Price distribution of products

Rating vs. category by Price analysis

Top 3 products

Rating vs category

Most reviewed products

Specifications comparison


