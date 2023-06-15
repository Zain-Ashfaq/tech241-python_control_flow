# Control flow

Control flow refers to the order in which statements are executed in a program. It allows for decision-making and branching based on specific conditions. In Python, control flow is commonly achieved using `if` and `elif` statements.

## if Statement

The if statement is used to execute a block of code if a given condition is true. Here's an example:

```python
# Example: Checking if a number is positive
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
```

## elif Statement

The elif statement is short for "else if" and is used to check additional conditions after the initial if statement. It allows for multiple conditions to be evaluated sequentially. Here's an example:

```python

# Example: Checking the range of a number
num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is positive.")
```
In this example, the program checks if the number is negative (num < 0), then if it's zero (num == 0), and if none of these conditions are true, it assumes the number is positive and executes the code in the else block.

The elif statement allows for multiple conditions to be evaluated and different code paths to be taken based on the outcome.

# Loops

You use for and while loops for iterative execution of code.

## For Loops

The `for` loop is used to iterate over a sequence (such as a list or a dictionary) or an iterable object. Here are some examples:

```python
# Example: Iterating over a list
list_data = [1, 2, 3, 4, 5]

for num in list_data:
    print(num)
```
In this example, the for loop iterates over each element in the list_data list and prints it.

```python

# Example: Iterating over an embedded list
embedded_lists = [[1, 2, 3], [4, 5, 6]]

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
```
This example demonstrates how to iterate over an embedded list. The outer loop iterates over each sublist, and the inner loop iterates over the numbers within each sublist.

```python

# Example: Iterating over a dictionary
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.36"},
    3: {"name": "Roscoe", "money": "$1.14"},
}

for item in dict_data.values():
    print(item)
    for embed_value, test in item.items():
        print(embed_value, test)
```
This example shows how to iterate over the values of a dictionary. The outer loop iterates over each dictionary value, and the inner loop iterates over the key-value pairs within each value.
## While Loops

The while loop is used to repeatedly execute a block of code as long as a specified condition is true. Here's an example:

```python

# Example: Simple while loop
x = 0

while x < 10:
    print(f"it is working -> {x}")
    x += 1
```
In this example, the while loop prints the current value of x and increments it until x becomes greater than or equal to 10.

```python

# Example: Using a while loop with a condition and break statement
x = 0

while x < 10:
    print(f"it is working -> {x}")
    if x == 4:
        break
    x += 1
```
This example demonstrates a while loop that includes a condition and a break statement. The loop will continue until x equals 4, at which point the break statement terminates the loop.

```python

# Example: Verifying user input with a while loop
user_prompt = True

while user_prompt:
    age = input("What is your age?\n")
    if age.isdigit() and int(age) < 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age}")
```
In this example, the while loop prompts the user to enter their age. It continues to prompt until a valid age (a digit less than 117) is provided.