import requests

print("--------Feedback Form--------")

while True:
    print("1.Submit Feedback")
    print("2.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        url="https://httpbin.org/post"
        n=input("Enter your name:")
        a=input("Enter your age:")
        feedback=input("Enter your feedback:")
        data={"name":n,"age":a,"feedback":feedback}
        r=requests.post(url,data=data)
    elif choice==2:
        break
    else:
        print("Invalid choice")

if r.status_code==200:
    print("Data sent successfully")
    print(r.json()["form"])
else:
    print("Data not sent")