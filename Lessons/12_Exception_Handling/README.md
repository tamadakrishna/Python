# Exception Handling

An exception is a runtime error that occurs during program execution and disrupts the normal flow of the program.

## Without exception handling:

    1. Program stops suddenly
    2. User gets error messages
    3. Program crashes


## With exception handling:
    1. Program continues safely
    2. Errors are handled gracefully
    3. User-friendly messages are shown

## Common Built-in Exception

| Exception           | Cause                  |
| ------------------- | ---------------------- |
| `ZeroDivisionError` | Divide by zero         |
| `ValueError`        | Invalid value          |
| `TypeError`         | Wrong data type        |
| `IndexError`        | Invalid list index     |
| `KeyError`          | Missing dictionary key |
| `FileNotFoundError` | File does not exist    |
| `NameError`         | Variable not defined   |

## Exception Flow
try → exception occurs → except → finally
try → no exception → else → finally
