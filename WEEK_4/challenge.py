# Step 1: Create and write to input.txt
with open("input.txt", "w") as file:
    file.write("This is the first line of text.\n")
    file.write("Python is an amazing programming language.\n")
    file.write("File handling is important in development.\n")
    file.write("Reading and writing files is a useful skill.\n")
    file.write("This challenge helps to practice file operations.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Process the content
word_count = len(content.split())  # Count words
uppercase_content = content.upper()  # Convert to uppercase

# Step 4: Write the processed content to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content)
    file.write(f"\n\nWord Count: {word_count}\n")

# Step 5: Print success message
print("Processing complete! 'output.txt' has been created successfully.")
