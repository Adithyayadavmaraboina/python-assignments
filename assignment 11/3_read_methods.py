# 3. Read file using read(), readline(), readlines()

print("----- Using read() -----")
file = open("sample.txt", "r")
content = file.read()
print(content)
print("Type of result:", type(content))
file.close()

print("\n----- Using readline() -----")
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
print("First call to readline():", line1, end="")
print("Second call to readline():", line2, end="")
file.close()

print("\n\n----- Using readlines() -----")
file = open("sample.txt", "r")
all_lines = file.readlines()
print(all_lines)
print("Type of result:", type(all_lines))
file.close()

print("""
Comparison:
- read()      -> returns the ENTIRE file content as a single string
- readline()  -> returns ONE line at a time as a string, moves cursor forward each call
- readlines() -> returns ALL lines as a LIST of strings, each element ends with '\\n'
""")
