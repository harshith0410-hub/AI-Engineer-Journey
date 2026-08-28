import requests

url="https://httpbin.org/post"

n=input("Enter your name:")
a=input("Enter your age:")

data={"name":n,"age":a}

r=requests.post(url,data=data)

if r.status_code==200:
    print("Data sent successfully")
    print(r.json()["form"])
else:
    print("Data not sent")  