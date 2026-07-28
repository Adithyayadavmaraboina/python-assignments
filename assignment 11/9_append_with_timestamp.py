# 9. Append data to a file, including the current date and time

from datetime import datetime

log_file = "log.txt"
message = "This is a new log entry."

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = f"[{current_time}] {message}\n"

with open(log_file, "a") as file:
    file.write(entry)

print("Entry appended to log file:")
print(entry, end="")

# show the full log file content
with open(log_file, "r") as file:
    print("\nFull content of log.txt:")
    print(file.read())
