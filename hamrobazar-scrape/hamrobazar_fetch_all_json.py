import json
import requests

url = "https://api.hamrobazaar.com/api/Product?PageSize=3300&CategoryId=F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50&IsHBSelect=false&PageNumber=1"
headers = {
    "User-Agent": "YourApp/1.0",
    "Authorization": "Bearer YourAccessToken",
    "Content-Type": "application/json",
    "Apikey": "09BECB8F84BCB7A1796AB12B98C1FB9E"
}


response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Request was successful")
    data = response.json()

    # Store the result in a JSON file
    with open("output_hamrobazaar/result.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

    print("Result has been saved to result.json")
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:", response.text)