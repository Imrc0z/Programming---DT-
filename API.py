#Rida Najibi.
#Het programma maakt gebruik van verschillende antivirus-engines om Malwares en Virussen te scannen.

import requests

#Hier kan je een API krijgen Key https://support.virustotal.com/hc/en-us/articles/115002100149-API

api_key = 'YOUR_API_KEY'
url = 'https://www.virustotal.com/vtapi/v2/file/scan'

# Specify the path to the file you want to scan
file_path = 'C:\\Users\\geena\\PycharmProjects\\Week 4\\venv\\Scripts\\python.exe'

try:
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        params = {'apikey': api_key}

        response = requests.post(url, files=files, params=params)

        if response.status_code == 200:
            result = response.json()
            print(result)
        else:
            print(f"Error: {response.status_code}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#Bij mogelijke permission error, run Pycharm als Administrator.