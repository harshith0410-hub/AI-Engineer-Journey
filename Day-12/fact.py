import requests
print("--------Fact--------")
url="https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
    print(f"Fact: {data['fact']}")
    print(f"Length: {data['length']}")
else:
    print(f"Error: Status Code {response.status_code}")