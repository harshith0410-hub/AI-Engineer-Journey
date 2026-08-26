import requests

print("------- QUOTE GENERATOR -------")

url = "https://zenquotes.io/api/random"

while True:

    print("\n1. Get Quote")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                print("\n📜 Quote")
                print(f"Quote  : {data[0]['q']}")
                print(f"Author : {data[0]['a']}")

            else:
                print(f"Error: Status Code {response.status_code}")

        except requests.exceptions.RequestException:
            print("Error: Please check your internet connection.")

    elif choice == "2":
        print("Thank you for using Quote Generator!")
        break

    else:
        print("Invalid choice. Please try again.")