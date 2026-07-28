# 7. Count words, lines, and characters in a file

file = open("sample.txt", "r")
content = file.read()
file.close()

lines = content.split("\n")
# remove a possible trailing empty line caused by a final newline character
if lines and lines[-1] == "":
    lines.pop()

words = content.split()
characters = len(content)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)
