# file_handling_assignment.py

# File Creation
try:
    # Create and open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text (including a mix of strings and numbers)
        file.write("This is the first line of text.\n")
        file.write("The second line contains a number: 42.\n")
        file.write("The third line includes a decimal number: 3.14.\n")

    print("File 'my_file.txt' created and data written successfully.")

except PermissionError:
    print("Error: You do not have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred while creating/writing to the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("Appending a new line: Python is awesome!\n")
        file.write("Another appended line: 100 is an integer.\n")
        file.write("Final appended line: 2.718 is a constant.\n")

    print("\nThree additional lines appended to 'my_file.txt'.")

except PermissionError:
    print("Error: You do not have permission to append to this file.")
except Exception as e:
    print(f"An unexpected error occurred while appending to the file: {e}")

# File Reading and Display after Appending
try:
    # Open the file again in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the updated contents of the file
        content = file.read()
        # Display the updated contents on the console
        print("\nUpdated contents of 'my_file.txt' after appending:")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file after appending: {e}")
