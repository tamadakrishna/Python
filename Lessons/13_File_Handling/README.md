# File Handling

## File Handling in Python means working with files to create, read, write, or modify data stored on your computer.

## Common modes 

| Mode  | Meaning                    |
| ----- | -------------------------- |
| `"r"` | Read (default)             |
| `"w"` | Write (creates/overwrites) |
| `"a"` | Append                     |
| `"x"` | Create new file            |
| `"b"` | Binary mode                |
| `"t"` | Text mode (default)        |


## File Methods

| Method        | Description        |
| ------------- | ------------------ |
| `read()`      | Reads file content |
| `write()`     | Writes to file     |
| `readline()`  | Reads one line     |
| `readlines()` | Reads all lines    |
| `close()`     | Closes file        |

## File Handling Exceptions

| Exception              | Cause                                          |
| ---------------------- | ---------------------------------------------- |
| `FileNotFoundError`    | File doesn’t exist                             |
| `IsADirectoryError`    | Tried to open a directory as a file            |
| `PermissionError`      | No permission to read/write file               |
| `OSError` / `IOError`  | General I/O problems (disk, OS errors)         |
| `EOFError`             | End-of-file reached unexpectedly (rare)        |
| `ValueError`           | Invalid operation (e.g., reading closed file)  |
| `UnsupportedOperation` | Operation not allowed in file mode             |
| `FileExistsError`      | Trying to create a file with `'x'` that exists |
