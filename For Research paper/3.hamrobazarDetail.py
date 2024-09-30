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
import re
import random

user_agent_list = [
        "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
        "Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",
        "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
        "Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    ]

SCRAPEOPS_API_KEY='14d5b493-bd02-4965-a467-e3b60154da4a'
 

# useragent = random.choice(user_agent_list)
# options = webdriver.ChromeOptions() #newly added 
# options.headless = True #newly added 
# proxy_options = {
#     'proxy': {
#         'http': f'http://scrapeops:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353',
#         'https': f'http://scrapeops:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353',
#         'no_proxy': 'localhost:127.0.0.1'
#     }
# }
# options.add_argument(f'--proxy-server={proxy_server_url}')
# options.add_argument(f"--proxy-server={proxy_options['proxy']['http']}")
# options.add_argument(f'user-agent={useragent}')
# # with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options ) as driver: #modified 
#     driver.maximize_window()        


options = webdriver.ChromeOptions() 
# options.add_argument('--headless')
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: #modified 
    driver.maximize_window()
    
    def is_page_fully_loaded(driver):
        return driver.execute_script("return document.readyState === 'complete';")

    folder_path = str(Path(__file__).parents[0])
    df = pd.read_excel('output_hamrobazaar/raw_data_backup.xlsx');
    # driver = selenium.webdriver.Chrome()

    row_array = df.to_numpy()
    updated_rows_df = pd.DataFrame(columns=df.columns)

    def slugify(input_string):
        # Convert to lowercase
        input_string = input_string.lower()
        # Remove special characters
        input_string = re.sub(r'[^a-z0-9]+', '-', input_string)
        # Remove leading and trailing hyphens
        input_string = input_string.strip('-')
        return input_string

    for index, eachRow in df[df['STATUS'] != 1].iterrows():

        if 'STATUS' not in eachRow or eachRow['STATUS'] != 1:
            brandName = slugify(eachRow['ADTITLE']) if not eachRow.get('BRANDNAME') or not isinstance(eachRow['BRANDNAME'], str) or not eachRow['BRANDNAME'].strip() else eachRow['BRANDNAME'].strip().lower()
            driver.get('https://hamrobazaar.com/cars/'+brandName+'/'+slugify(eachRow['ADTITLE'])+'/'+eachRow['ID'].lower());
            url='https://hamrobazaar.com/cars/'+brandName+'/'+slugify(eachRow['ADTITLE'])+'/'+eachRow['ID'].lower();
            WebDriverWait(driver, 5).until(lambda x: is_page_fully_loaded(x))
            features="";
            df.at[index, 'URL'] = url
            df.at[index, 'STATUS'] = 1

            try:
                specificationsElement = driver.find_element(By.XPATH,'//*[@id="hb__root"]/div[2]/main/div/section/div[3]/div/div[3]/div');
                eachSpecificationList=specificationsElement.find_elements(By.CLASS_NAME,'feature__item');
                for eachFeatures in eachSpecificationList:
                    featureTitle= eachFeatures.find_element(By.CSS_SELECTOR,'div.label>span').text;
                    featureVal= eachFeatures.find_element(By.CSS_SELECTOR,'div.label__desc>span').text;
                    df.at[index, featureTitle] = str(featureVal)
                    features += ""+featureTitle+":"+str(featureVal)+',\n'
                df.at[index, 'allFeatures'] = features
            except NoSuchElementException:
                df.to_excel('output_hamrobazaar/initia_raw_data.xlsx', index=False)
                df.to_excel('output_hamrobazaar/raw_data_backup.xlsx', index=False)
                continue
            
            df.to_excel('output_hamrobazaar/initial_raw_data.xlsx', index=False)
            df.to_excel('output_hamrobazaar/raw_data_backup.xlsx', index=False)

            time.sleep(1);




            
    