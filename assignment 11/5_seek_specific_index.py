# 5. Read from a specific index using seek(), fixed number of characters

file = open("sample.txt", "r")

start_index = 6
num_chars = 5

file.seek(start_index)
data = file.read(num_chars)

print(f"Jumping to index {start_index} and reading {num_chars} characters:")
print(data)   # should print "World" since sample.txt starts with "Hello World"

file.close()
