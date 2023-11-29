import json
import pandas as pd

# Load JSON data from the file
with open("output_hamrobazaar/allCarList.json", "r") as json_file:
    data = json.load(json_file)

# Extracting desired data
extracted_data = []
for car in data['data']:
    car_data = {
        "brandName": car["brandName"],
        "adsTitle": car["name"],
        "id": car["id"],
        "createdOn": car["createdOn"],
        "condition": car["condition"],
        "price": car["price"],
        "description": car["description"],
        "locationDescription": car["location"]["locationDescription"],
        "createdBy": car["creatorInfo"]["createdBy"]
    }
    extracted_data.append(car_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(extracted_data)

# Save the DataFrame to an Excel file
df.to_excel("output_hamrobazaar/initial_data.xlsx", index=False)