# 1. Read a text file

file = open("sample.txt", "r")
content = file.read()
print("Contents of the file:\n")
print(content)
file.close()
