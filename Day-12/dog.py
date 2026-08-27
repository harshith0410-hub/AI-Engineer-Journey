import requests
print("-------Dog Pictures--------")

url="https://dog.ceo/api/breeds/image/random"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print(f"Dog image: {data['message']}")
    print(f"Dog status: {data['status']}")
else:
    print(f"Error: {response.status_code}") 