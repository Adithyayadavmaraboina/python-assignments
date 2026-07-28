# 2. Write to a text file (using 'w' and 'a' modes)

# 'w' mode - creates a new file or overwrites existing content
user_text = "This is my first line written to the file."

file = open("output.txt", "w")
file.write(user_text)
file.close()
print("Data written using 'w' mode (file created/overwritten)")

# 'a' mode - appends to the existing content instead of overwriting
more_text = "\nThis is an additional line appended to the file."

file = open("output.txt", "a")
file.write(more_text)
file.close()
print("Data written using 'a' mode (appended to existing file)")

# read back to confirm
with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())

# NOTE: In an interactive script you would normally use:
# user_text = input("Enter text to write to the file: ")
# But since this runs non-interactively here, a fixed string is used above.
