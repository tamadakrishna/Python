# Conditions in Python
x = 10
y = 20
# Simple if statement
if x < y:
    print("x is less than y")




# if-else statement
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")




# if-elif-else statement
if x == y:
    print("x is equal to y")
elif x < y:
    print("x is less than y")
else:
    print("x is greater than y")   




# Nested if statement
if x < 15:
    if y > 15:
        print("x is less than 15 and y is greater than 15") 



# Using logical operators
if x < 15 and y > 15:
    print("x is less than 15 and y is greater than 15")
if x < 5 or y > 15:
    print("Either x is less than 5 or y is greater than 15")




# Ternary operator
result = "x is less than y" if x < y else "x is not less than y"
print(result)   





# Membership operator
numbers = [10, 20, 30, 40]
if x in numbers:
    print("x is in the list of numbers")
if 50 not in numbers:
    print("50 is not in the list of numbers")





# Identity operator
a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object")
if a is not [1, 2, 3]:
    print("a and [1, 2, 3] do not refer to the same object")






# Using pass statement
if x > y:
    pass  # Placeholder for future code
else:
    print("x is not greater than y")





# Using the match-case statement (Python 3.10+)
value = 2
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3:
        print("Value is 3")
    case _:
        print("Value is something else")  





# Using assert statement
assert x < y, "x should be less than y" 
print("Assertion passed: x is less than y") 

