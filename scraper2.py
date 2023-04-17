from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/gopui/Downloads/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

temp_list = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source, "html.parser")
        starTable = soup.find("table")
        
        table_rows = starTable.find_all("tr")
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

# Calling Method    
scrape()

# Define Header
headers = ["name", "distance", "mass", "radius"]

# Define pandas DataFrame   
df = pd.DataFrame(temp_list)



# Convert to CSV
df.to_csv("scraped_data_1.csv", index = True, index_label = "id")
    


