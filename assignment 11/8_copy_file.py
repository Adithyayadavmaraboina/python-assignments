# 8. Copy content from one file to another

source_file = "sample.txt"
destination_file = "sample_copy.txt"

with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print(f"Content copied from '{source_file}' to '{destination_file}' successfully")

# verify by reading the new file
with open(destination_file, "r") as file:
    print("\nContent of the copied file:")
    print(file.read())
