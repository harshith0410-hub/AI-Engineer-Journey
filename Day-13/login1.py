import requests

print("-------- LOGIN FORM --------")

url = "https://httpbin.org/post"

while True:

    print("\n1. Login")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:

            print("\nLogin request sent successfully!")

            received = response.json()["json"]

            print(f"Username: {received['username']}")
            print(f"Password: {received['password']}")

            again = input("\nDo you want to login again? (y/n): ").lower()

            if again == "n":
                print("Thank you for using the Login Form!")
                break

        else:
            print(f"Error: {response.status_code}")

    elif choice == 2:
        print("Thank you for using the Login Form!")
        break

    else:
        print("Invalid choice. Please try again.")