# 4. Random access file reading using seek()

file = open("sample.txt", "r")

print("Reading from the beginning:")
print(file.read(11))   # reads first 11 characters -> "Hello World"

print("\nMoving cursor to position 12 using seek()")
file.seek(12)

print("Reading from position 12 onward:")
print(file.read())

file.close()
