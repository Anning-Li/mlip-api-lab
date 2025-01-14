import requests
import json


url = "http://localhost:3000/api/v1/analysis/"


json_data = {
    "uri": "https://spiralcute.com/characters/chiikawa/en/img/main.jpg"
}

response = requests.get(url, headers={"Content-Type": "application/json"}, data=json.dumps(json_data))

print("Status Code:", response.status_code)
print("Response:", response.text)

