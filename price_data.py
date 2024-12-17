import requests
import json
import os

def fetch_data():
    endpoint_url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
    headers = {
        'User-Agent': 'GP Predict v1.0',
        'From': 'tysonthetyrant@gmail.com'  # Optional valid field
    }
    response = requests.get(endpoint_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        extracted_data = {}

        # Extracting all keys and formatting
        for key, value in data.get('data', {}).items():
            extracted_data[key] = [
                value.get("high"),
                value.get("highTime"),
                value.get("low"),
                value.get("lowTime")
            ]

        # Construct the path to save the formatted data
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(script_dir, 'data', 'gp_data.json')

        # Save the formatted data
        with open(data_file_path, "w") as file:
            json.dump(extracted_data, file, indent=4)
        print("Data successfully saved!")

    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_data()
