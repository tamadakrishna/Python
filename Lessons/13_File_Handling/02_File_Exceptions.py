# File Handling in Python with Exception Handling

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.txt")

try:
    # Attempt to open the file
    with open(FILE_PATH, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file at {FILE_PATH} was not found.")
except IOError:
    print(f"Error: An I/O error occurred while handling the file at {FILE_PATH}.")
else:
    print("File read successfully without any errors.")
finally:
    print("Execution of file handling is complete.")



# | Exception              | Cause                                          |
# | ---------------------- | ---------------------------------------------- |
# | `FileNotFoundError`    | File doesn’t exist                             |
# | `IsADirectoryError`    | Tried to open a directory as a file            |
# | `PermissionError`      | No permission to read/write file               |
# | `OSError` / `IOError`  | General I/O problems (disk, OS errors)         |
# | `EOFError`             | End-of-file reached unexpectedly (rare)        |
# | `ValueError`           | Invalid operation (e.g., reading closed file)  |
# | `UnsupportedOperation` | Operation not allowed in file mode             |
# | `FileExistsError`      | Trying to create a file with `'x'` that exists |
# | `BlockingIOError`     | Non-blocking operation would block             |
# | `TimeoutError`         | File operation timed out                        |
# | `MemoryError`          | Not enough memory to complete file operation   |
# | `UnicodeDecodeError`   | Error decoding file content                     |
# | `UnicodeEncodeError`   | Error encoding content to write to file        |

