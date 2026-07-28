# 6. Check file permissions using os.access()

import os

filename = "sample.txt"

if os.path.exists(filename):
    readable = os.access(filename, os.R_OK)
    writable = os.access(filename, os.W_OK)

    print(f"File: {filename}")
    print("Read permission:", readable)
    print("Write permission:", writable)
else:
    print(f"File '{filename}' does not exist")
