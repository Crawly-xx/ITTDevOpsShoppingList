# Open the file for reading and writing
file = open("list.txt", "r+")

existing_contents = file.read().splitlines()

while True:
    # Prompt the user for input
    print("Enter some items to add on to the shopping list (enter quit to Quit): ")
    data = input()

    # Check if the user wants to quit
    if data == "quit":
        print("Exiting program...")
        break

    
    if data in existing_contents:
        print("Is already in the shopping list, skipping input")
    else:
        # Write the user's input to the file
        file.write(data + "\n")

        existing_contents.append(data)

        print(data + " added to list successfully!")

# Close the file
file.close()
