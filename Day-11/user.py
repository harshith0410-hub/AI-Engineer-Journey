import json
import requests

print("-----GIT USER FINDER-----")
username=input("Enter your Github user name")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code==200:
    data=response.json()
    print(f"Name: {data['name']}")
    print(f"Username: {data['login']}")
    print(f"Company: {data['company']}")
    print(f"Email: {data['email']}")
    print(f"Location: {data['location']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
    print(f"Public Repos: {data['public_repos']}")
   
else:
    print("User not found")