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


options = webdriver.ChromeOptions() #newly added 
options.headless = True #newly added 
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: #modified 

    def is_page_fully_loaded(driver):
        return driver.execute_script("return document.readyState === 'complete';")

    folder_path = str(Path(__file__).parents[0])
    df = pd.read_excel('output/output_data_init.xlsx');
    # driver = selenium.webdriver.Chrome()

    row_array = df.to_numpy()
    updated_rows_df = pd.DataFrame(columns=df.columns)


    for index, eachRow in df.iterrows():
        if(eachRow['Status']!=1):
            driver.get(eachRow[0]);
            WebDriverWait(driver, 1).until(lambda x: is_page_fully_loaded(x))
            data={};
            features="";
            brand = driver.find_element(By.XPATH,'/html/body/main/div[1]/div[1]/div/div/div[1]/nav/ol/li[3]').text;
            try:
                price= driver.find_element(By.XPATH,'/html/body/main/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/span/span').text;
            except NoSuchElementException:
                price= "Null"
            try:
                description= driver.find_element(By.CSS_SELECTOR,'.ad-seller-comment >* p').text;
            except NoSuchElementException:
                description= "Null"
            try:
                sellerPhone=driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[2]/div[1]/div[7]/div[2]/div/span').text
            except NoSuchElementException:
                sellerPhone= "Null"

            # Add a new column named 'new_column' with the value 'abc'
            df.at[index, 'BRANDS'] = brand
            df.at[index, 'SELLERPHONE'] = sellerPhone
            df.at[index, 'Price-inner'] = price
            df.at[index, 'description'] = description
            allFeatures= driver.find_elements(By.CSS_SELECTOR,'.vehicle-properties > .prop');
            for eachFeatures in allFeatures:
                featureTitle= eachFeatures.find_element(By.CSS_SELECTOR,'span:nth-child(1)').text;
                featureVal= eachFeatures.find_element(By.CSS_SELECTOR,'span:nth-child(2)').text;
                df.at[index, featureTitle] = featureVal
                features += ""+featureTitle+":"+featureVal+',\n'
            # data={"brand":brand,"price":price,"sellerPhone":sellerPhone,"features":features};
            # length=len(eachRow);
            df.at[index, 'FEATURES'] = features
            df.at[index, 'Status'] = 1
        # Write the updated DataFrame to the same Excel file
            df.to_excel('output/nepalicarsData.xlsx', index=False)



    