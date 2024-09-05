import json
import requests

# API endpoint and headers
url = "https://api.hamrobazaar.com/api/Product"
headers = {
    "User-Agent": "YourApp/1.0",
    "Authorization": "Bearer YourAccessToken",
    "Content-Type": "application/json",
    "Apikey": "09BECB8F84BCB7A1796AB12B98C1FB9E"
}

# Set initial parameters
page_size = 10  # Limit to 10 records per page
page_number = 1  # Start with the first page
all_data = []  # List to store all records

# First API call to get the total number of pages
initial_response = requests.get(f"{url}?CategoryId=F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50&IsHBSelect=false&PageSize={page_size}&PageNumber={page_number}", headers=headers)

if initial_response.status_code == 200:
    initial_data = initial_response.json()

    if 'totalPages' in initial_data:
        total_pages = initial_data['totalPages']
        print(f"Total Pages: {total_pages}")

        # Loop through all pages
        for page in range(1, total_pages + 1):
            print(f"Fetching page {page} of {total_pages}")
            response = requests.get(f"{url}?CategoryId=F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50&IsHBSelect=false&PageSize={page_size}&PageNumber={page}", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    all_data.extend(data['data'])  # Append data from current page
                else:
                    print(f"Unexpected data structure: {data}")
                    break
        
        # Save the merged data into a single JSON file
        with open("output_hamrobazaar/allCarList.json", "w") as json_file:
            json.dump(all_data, json_file, indent=2)
        print("Data saved to allCarList.json")
    else:
        print("'totalPages' key not found in the response.")
else:
    print(f"Failed to retrieve data. Status code: {initial_response.status_code}")
