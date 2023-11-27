from selenium import webdriver
import selenium.webdriver
import os
from pathlib import Path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pandas as pd




folder_path = str(Path(__file__).parents[0])
driver = selenium.webdriver.Chrome()
driver.get("https://www.nepalicars.com/en/vehicle_listings");


data=[]
totalPages=driver.find_element(By.XPATH,'//*[@id="ads-list"]/div[7]/div/a[5]').text;


def getData(adsList):
    
    allAdsHref= adsList.find_elements(By.CSS_SELECTOR,'a.common-ad-card');
    for eachHrefs in allAdsHref:
        url= eachHrefs.get_attribute('href')
        title= eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > .specification-section > h4').text;
        price= eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification  > * .ad-vehicle-price > .value').text;
        try:
            mileage = eachHrefs.find_element(By.CSS_SELECTOR, '.ad-specification > * .ad-vehicle-mileage > * .value').text
        except NoSuchElementException:
            mileage = "Null"
        fuel=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-vehicle-engine >.engine-capacity > span:nth-child(3)').text;
        transmission=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-vehicle-engine >.transmission > span').text;
        dateOfPost=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-post-date  > span').text;
        try:
            description=eachHrefs.find_element(By.CSS_SELECTOR, '.ad-specification > * .sort-ad-description').text
        except NoSuchElementException:
            description= "Null"
        
        newRow={"url":url, "title": title, "price":price, "mileage":mileage, "fuel":fuel,"transmission":transmission,"dateOfPost":dateOfPost,"description":description}
        data.append(newRow);

def is_page_fully_loaded(driver):
    return driver.execute_script("return document.readyState === 'complete';")

for eachPage in range(2, int(totalPages)):
    
    driver.get("https://www.nepalicars.com/en/vehicle_listings?page="+str(eachPage));
    WebDriverWait(driver, 15).until(lambda x: is_page_fully_loaded(x))

    adsList=driver.find_element(By.ID,'ads-list');
    getData(adsList);

driver.quit()

# Convert the 'data' list to a pandas DataFrame
df = pd.DataFrame(data)

# Specify the Excel file path and name
excel_file_path = 'output/output_data.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Data written to {excel_file_path}")
                
        
     