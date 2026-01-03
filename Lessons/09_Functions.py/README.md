# Function

A function is a block of reusable code that performs a specific task.

Usage:
- Avoid code repetition

- Improve readability

- Make programs easier to maintain

## Syntax
def function_name(parameters):
    # function body
    return value

   - def → keyword to define a function

   - parameters → input values (optional)

   - return → sends result back (optional)


# Function Annotations

Function annotations are optional metadata about:

    - Function parameters

    - Return value

They do NOT enforce types at runtime

Mainly used for:

    - Documentation

    - Type checking tools

    - Better IDE support

# Basic Syntax
def function_name(parameter: type) -> return_type:
    return value

Refer: 02_Function_Annotation.py