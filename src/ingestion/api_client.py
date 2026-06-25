import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("CRIC_API_KEY")

URL = "https://api.cricapi.com/v1/matches"

params = {
    "apikey": API_KEY,
    "offset": 0
}

print("Fetching match data...")

response = requests.get(URL, params=params)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:

    data = response.json()

    print("API Response Status:", data.get("status"))

    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/matches.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ Match data saved to data/raw/matches.json")

else:
    print("❌ Failed to fetch data")