print("---------Personal Note Management System---------")

while True:
    print("\nWelcome to the Personal Note Management System!")
    print("Enter 1. Add Note")
    print("Enter 2. View Notes")
    print("Enter 3. Delete Note")
    print("Enter 4. Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        note = input("Enter your note: ")

        with open("notes.txt", "a") as f:
            f.write(note + "\n")

        print("Note added successfully!")

    elif n == 2:
        with open("notes.txt", "r") as f:
            lines = f.readlines()

        if len(lines) == 0:
            print("No notes available.")
        else:
            print("\n--------- Your Notes ---------")

            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

    elif n == 3:
        with open("notes.txt", "r") as f:
            lines = f.readlines()

        if len(lines) == 0:
            print("No notes available to delete.")

        else:
            print("\n--------- Your Notes ---------")

            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

            note_number = int(
                input("Enter the line number of the note you want to delete: ")
            )

            if 1 <= note_number <= len(lines):

                del lines[note_number - 1]

                with open("notes.txt", "w") as f:
                    f.writelines(lines)

                print("Note deleted successfully!")

            else:
                print("Invalid note number!")

    elif n == 4:
        print("Thank you for using the Personal Note Management System!")
        break

    else:
        print("Invalid choice!")
        continue

    print("\nDo you want to continue?")
    c = input("Enter Y for yes and N for no: ")

    if c == "Y" or c == "y":
        continue
    else:
        break

print("Thank you for using the Personal Note Management System!")