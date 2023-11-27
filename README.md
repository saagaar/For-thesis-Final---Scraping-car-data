
# Scraping hamrobazaar.com and nepalicars.com 

 This is the code for scraping hamrobazaar.com and nepalicars.com for the partial fulfilment of academic thesis on topic  **Price Determination and Prediction of Used Vehicles  In Nepal** 

 ## Technologies Used
 - Python as a programming language
 - Pandas to read and write data from and to excel sheet
 - Selenium (Browser Automation tool)
 - pip (Python Package manager)
 - venv(Virtual Environment for Python)

**How to run?**
- First install python3(recommended) in your computer or install any other versions
- Install **PIP**. If you have python3 or later version you already have **pip** a pacakge manager for python comes by default or else install pip
- Install **venv** using pip by:
  
  ```$ sudo pip install virtualenv```

  **What is virtual env?**

> venv (for Python 3) allows you to manage separate package installations for different projects. It creates a “virtual” isolated Python installation. When you switch projects, you can create a new virtual environment which is isolated from other virtual environments. You benefit from the virtual environment since packages can be installed confidently and will not interfere with another project’s environment.

Once Virtual env is setup you need to create virtual env for the given project i.e. 

   ```$ python3 -m venv <virtualenv>```
  
   This will create a folder with name virtual env and create your virtual env where you can manage all of your project dependencies.

   Now once this folder is created you need to activate this venv using following command:

     $ source virtualenv/bin/activate
     
   Now finally you are ready to install all the dependencies for this project which are saved in a file named requirements.txt , You can install all of these dependencies using 

    $  pip install -r  requirements.txt

Now we are ready to scrape our data:
 
 ## Scraping  nepalicars.com
 Since we require all the available data of used cars so we needed data from listing page i.e. https://www.nepalicars.com/en/vehicle_listings  and also some data needed to be scraped from detail of each cars data.
 
 The file **nepalicars.py** includes code to  scrap data from listing page which scrapes all the lists with scraping from paginated data which is saved to a excel sheet inside output_nepalicars/output_data_init.xlsx
 
 The file  **nepalicardetail.py** includes code to scrap data from each row of excelsheet from output_data_init.xlsx and new data are scraped from detail page and added to the same row of data in output_Data_init.xlsx and finally written to nepalicarsData.xlsx 

 We fetched total of 901 data from nepalicars.com .


 The code was updated on **27th November 2023**

 
 
