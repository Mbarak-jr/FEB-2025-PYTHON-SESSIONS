def modify_content(content):
    """Modify content by converting it to uppercase."""
    return content.upper()


def read_and_write_file():
    """Reads a file, modifies content, and writes it to a new file."""
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = modify_content(content)
        new_filename = "modified_" + filename

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(
            f"File '{filename}' read successfully. Modified content saved to '{new_filename}'.")

    except FileNotFoundError:
        print(
            f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(
            f"Error: Permission denied. You don't have access to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_and_write_file()
