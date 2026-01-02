# Operators

# Arithmetic Operators
Used for mathematical calculations.

| Operator | Meaning        | Example  | Result |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 2`  | 7      |
| `-`      | Subtraction    | `5 - 2`  | 3      |
| `*`      | Multiplication | `5 * 2`  | 10     |
| `/`      | Division       | `5 / 2`  | 2.5    |
| `//`     | Floor division | `5 // 2` | 2      |
| `%`      | Modulus        | `5 % 2`  | 1      |
| `**`     | Exponent       | `5 ** 2` | 25     |


# Assignment Operators
Used to assign values to variables.

| Operator | Meaning             | Example   |
| -------- | ------------------- | --------- |
| `=`      | Assign              | `x = 5`   |
| `+=`     | Add and assign      | `x += 2`  |
| `-=`     | Subtract and assign | `x -= 2`  |
| `*=`     | Multiply and assign | `x *= 2`  |
| `/=`     | Divide and assign   | `x /= 2`  |
| `//=`    | Floor divide assign | `x //= 2` |
| `%=`     | Modulus assign      | `x %= 2`  |
| `**=`    | Exponent assign     | `x **= 2` |

# Comparison Operators
Used to compare two values. Returns True or False.

| Operator | Meaning          | Example  | Result |
| -------- | ---------------- | -------- | ------ |
| `==`     | Equal            | `5 == 5` | True   |
| `!=`     | Not equal        | `5 != 2` | True   |
| `>`      | Greater than     | `5 > 2`  | True   |
| `<`      | Less than        | `5 < 2`  | False  |
| `>=`     | Greater or equal | `5 >= 5` | True   |
| `<=`     | Less or equal    | `5 <= 2` | False  |


# Logical Operators
Used to combine boolean expressions.

| Operator | Meaning     | Example          | Result |
| -------- | ----------- | ---------------- | ------ |
| `and`    | Logical AND | `True and False` | False  |
| `or`     | Logical OR  | `True or False`  | True   |
| `not`    | Logical NOT | `not True`       | False  |

# Bitwise Operators
Operate on binary numbers (0 and 1).

| Operator | Meaning     | Example  | Result |    
| -------- | ----------- | -------- | ------ | 
| `&`      | AND         | `5 & 3`  | 1      | 
| `|`      | OR          | `5 | 3`  | 7      |    
| `^`      | XOR         | `5 ^ 3`  | 6      |
| `~`      | NOT         | `~5`     | -6     |
| `<<`     | Left shift  | `5 << 1` | 10     |
| `>>`     | Right shift | `5 >> 1` | 2      |

# Membership Operators
Check if a value exists in a sequence.

| Operator | Meaning            | Example            | Result |
| -------- | ------------------ | ------------------ | ------ |
| `in`     | Exists in sequence | `'a' in 'cat'`     | True   |
| `not in` | Does not exist     | `'x' not in 'cat'` | True   |

# Identity Operators
Check if two variables refer to the same object in memory.

| Operator | Meaning             | Example      | Result     |
| -------- | ------------------- | ------------ | ---------- |
| `is`     | Same object         | `a is b`     | True/False |
| `is not` | Not the same object | `a is not b` | True/False |



# Operator Precedence (Optional Advanced)

Python evaluates operators in this order (high → low):

1. () Parentheses
2. ** Exponent
3. *, /, //, %
4. +, -
5. Bitwise operators
6. Comparison operators
7. Logical not → and → or
8. Assignment operators