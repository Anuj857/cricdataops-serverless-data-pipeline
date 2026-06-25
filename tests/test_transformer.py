import json

from src.transformation.transformer import transform_match

with open("data/raw/matches.json", "r", encoding="utf-8") as file:
    data = json.load(file)

first_match = data["data"][0]

clean_match = transform_match(first_match)

print(clean_match)