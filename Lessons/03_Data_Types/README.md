# Python Data Types (Built-in)

Python has several core data types that represent single values.

## Numeric Types
| Type      | Description                     | Example      |
| --------- | ------------------------------- | ------------ |
| `int`     | Integer numbers (whole numbers) | `x = 10`     |
| `float`   | Decimal numbers                 | `y = 3.14`   |
| `complex` | Complex numbers (`a + bj`)      | `z = 2 + 3j` |


## Text Type
| Type  | Description            | Example          |
| ----- | ---------------------- | ---------------- |
| `str` | Sequence of characters | `name = "Alice"` |


## Boolean Type
| Type   | Description             | Example           |
| ------ | ----------------------- | ----------------- |
| `bool` | Represents True / False | `is_happy = True` |

## None Type
| Type       | Description                   | Example    |
| ---------- | ----------------------------- | ---------- |
| `NoneType` | Represents absence of a value | `x = None` |

# Bytes & Memory Types (Optional / Specialized)
| Type        | Description                     | Example           |
| ---------   | ------------------------------- | ----------------  |
| `bytes`     | Immutable sequence of bytes     | `b"hello"`        |
| `bytearray` | Mutable sequence of bytes       | `bytearray(b"hi")`|
| `memoryview`| Access memory of another object | `memoryview(b"hi")`|
