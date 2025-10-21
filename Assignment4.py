# File Read & Write with Error Handling

def modify_file_content(text):
    """
    A simple function that modifies the file content.
    Example: converts text to uppercase.
    """
    return text.upper()


def read_and_write_file():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Create a new output file
        output_filename = "modified_" + input_filename

        # Write modified content into the new file
        with open(output_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Successfully created '{output_filename}' with modified content!")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("⚠️ Error: You don't have permission to read or write this file.")
    except Exception as e:
        print(f"⚡ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    read_and_write_file()
