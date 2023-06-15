# https://trello.com/c/mGs3xIzy/65-control-flow-task-4-while-loops-optional

# Taking 10 integers and printing their average
count = 0
total = 0

while count < 10:
    num = int(input("Enter an integer: "))
    total += num
    count += 1

average = total / 10
print("Average value:", average)

# Printing a series of numbers upto 300
num = 10

while num <= 300:
    print(num)
    num += 10

# Upgrading waiter program with menu validation
menu = ['pizza', 'burger', 'pasta', 'salad']
order = []
print("Menu:\n")
for item in menu:
    print(item)

print("Enter 0 to finish the order.")

while True:
    item = input("Enter an item: ")
    if item == '0':
        break
    elif item in menu:
        order.append(item)
    else:
        print("Item not available in the menu. Please choose again.")

for item in order:
    print(item)

# Taking input until user enters 0 and summing positive and negative numbers
positive_sum = 0
negative_sum = 0

while True:
    num = int(input("Enter 0 to quit otherwise add a number:\n "))
    if num == 0:
        break
    elif num > 0:
        positive_sum += num
    else:
        negative_sum += num

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
