from selenium import webdriver
import selenium.webdriver
import os
from pathlib import Path
import time
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import numpy as np



options = webdriver.ChromeOptions() 
# options.add_argument('--headless')
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: #modified 
    driver.maximize_window()
    # driver.set_window_size(2560, 1600) 
    driver.get("https://hamrobazaar.com/category/cars/EB9C8147-07C0-4951-A962-381CDB400E37/F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50");
   
    data=[]
    dataIndex=0;
    def is_page_fully_loaded(driver):
        return driver.execute_script("return document.readyState === 'complete';")

    WebDriverWait(driver, 1).until(lambda x: is_page_fully_loaded(x))
    allElement = driver.find_element(By.CLASS_NAME,'product-list');

    # index=allElement.findChildElements()get_attribute('data-index');
    # print(index)
    def getDataElement():
        allCardElements=driver.find_elements(By.XPATH,'//*[@id="hb__root"]/div[2]/div[2]/div[1]/section/div[2]/div/div/div[1]/div');
        for index, eachElements in allCardElements:
            # print(eachElements);
            indexCount=eachElements.get_attribute('data-index');
            anchor=eachElements.find_element(By.CSS_SELECTOR,'.nameAndDropdown > a').get_attribute('href');
            title=eachElements.find_element(By.CSS_SELECTOR,'.nameAndDropdown >a >h2').text;
            brand=eachElements.find_element(By.CSS_SELECTOR,'.nameAndDropdown >a >h2 >small').text;
            description=eachElements.find_element(By.CSS_SELECTOR,'p.description').text;
            price=eachElements.find_element(By.CSS_SELECTOR,'.priceAndCondition >* span.regularPrice').text;
            condition=eachElements.find_element(By.CSS_SELECTOR,'.priceAndCondition > span.condition').text;
            # timeAgo=eachElements.find_element(By.CSS_SELECTOR,'.locationAndTime span.time').text;
            print(condition+' '+price);
        return index;

    # if(dataIndex<3500){
    #     dataIndex=getDataElement();
    # }
    getDataElement();
    # dataIndex=getDataElement();

        # if(allElement.get_attribute())
    # print(index)
    # driver.scroll_from_origin('ScrollOrigin',20);
    # def getData(adsList):
        
    #     allAdsHref= adsList.find_elements(By.CSS_SELECTOR,'a.common-ad-card');
    #     
    #         url= eachHrefs.get_attribute('href')
    #         title= eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > .specification-section > h4').text;
    #         price= eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification  > * .ad-vehicle-price > .value').text;
    #         try:
    #             mileage = eachHrefs.find_element(By.CSS_SELECTOR, '.ad-specification > * .ad-vehicle-mileage > * .value').text
    #         except NoSuchElementException:
    #             mileage = "Null"
    #         fuel=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-vehicle-engine >.engine-capacity > span:nth-child(3)').text;
    #         transmission=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-vehicle-engine >.transmission > span').text;
    #         dateOfPost=eachHrefs.find_element(By.CSS_SELECTOR,'.ad-specification > * .ad-post-date  > span').text;
    #         try:
    #             description=eachHrefs.find_element(By.CSS_SELECTOR, '.ad-specification > * .sort-ad-description').text
    #         except NoSuchElementException:
    #             description= "Null"
            
    #         newRow={"url":url, "title": title, "price":price, "mileage":mileage, "fuel":fuel,"transmission":transmission,"dateOfPost":dateOfPost,"description":description}
    #         data.append(newRow);

    # def is_page_fully_loaded(driver):
    #     return driver.execute_script("return document.readyState === 'complete';")

    # for eachPage in range(2, int(totalPages)):
        
    #     driver.get("https://www.nepalicars.com/en/vehicle_listings?page="+str(eachPage));
    #     WebDriverWait(driver, 15).until(lambda x: is_page_fully_loaded(x))

    #     adsList=driver.find_element(By.ID,'ads-list');
    #     getData(adsList);

    # driver.quit()

    # # Convert the 'data' list to a pandas DataFrame
    # df = pd.DataFrame(data)

    # # Specify the Excel file path and name
    # excel_file_path = 'output/output_data.xlsx'

    # # Write the DataFrame to an Excel file
    # df.to_excel(excel_file_path, index=False)

    # print(f"Data written to {excel_file_path}")
                    
            
        