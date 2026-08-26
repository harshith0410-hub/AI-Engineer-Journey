import json
import requests
print("-------RANDOM JOKE SYSTEM-------")

url="https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
data = response.json()
print(response.status_code)
print(data.keys())
print(data["type"])

print(f"Question: {data['setup']}")
print(f"Answer: {data['punchline']}")