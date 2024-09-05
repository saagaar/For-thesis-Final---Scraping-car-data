import json
import pandas as pd

# Load JSON data from the file
with open("output_hamrobazaar/allCarList.json", "r") as json_file:
    data = json.load(json_file)
# Extracting desired data
extracted_data = []
for car in data:
    car_data = {
        "ID": car["id"],
        "BRANDNAME": car["brandName"],
        "ADTITLE": car["name"],
        "CREATEDON": car["createdOn"],
        "CREATEDONHUMAN": car["createdOn"],
        "CONDITION": car["condition"],
        "PRICE": car["price"],
        "DESCRIPTION": car["description"],
        "LOCATION": car["location"]["locationDescription"],
        "CREATEDBY": car["creatorInfo"]["createdByName"],
        "STATUS":0
    }
    
    extracted_data.append(car_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(extracted_data)

# Save the DataFrame to an Excel file
df.to_excel("output_hamrobazaar/initial_data.xlsx", index=False)