# https://trello.com/c/TEKLVsOF/63-control-flow-task-3-loops-and-lists

# Looping with range
for i in range(10):
    print("Hello")

# Creating a list of names
list_names = []
for i in range(5):
    name = input("Enter a name: ")
    list_names.append(name)

# Creating a new list with lowercase names
list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())

for i in list_names_lower:
    print(i)


# Printing even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Change the list as per your requirement
for num in numbers:
    if num % 2 == 0:
        print(num)

# Summing numbers from 0 to 100
sum_total = 0
for num in range(101):
    sum_total += num
print("Sum of numbers from 0 to 100:", sum_total)

# Summing odd and even numbers separately
sum_odd = 0
sum_even = 0
for num in range(101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of odd numbers from 0 to 100:", sum_odd)
print("Sum of even numbers from 0 to 100:", sum_even)
