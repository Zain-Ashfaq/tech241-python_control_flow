# # for and while loops
#
# # in python we just use for
#
# list_data = [1,2,3,4,5]
# embedded_lists = [[1,2,3], [4,5,6]]
#
# dict_data = {
#     1: {"name": "Bronson", "money":"$0.05"},
#     2: {"name": "Masha", "money":"$3.36"},
#     3: {"name": "Roscoe", "money":"$1.14"},
# }
#
# # for num in list_data:
# #     print(num)
#
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)
#
# for item in dict_data.values():
#     print(item)
#     for embed_value, test in item.items():
#         print(embed_value,test)
#
# # a loop that only returns money
#
# for items in dict_data.values():
#     print(items["money"])
#
#
# # loops and if statements
#
# for num in list_data:
#     if num == 3:
#         print("You have found three!")
#
#     elif num > 3:
#         print("Gone too far")
#     else:
#         print("too soon")

# While Loops

x = 0

# while x < 10:
#     print(f"it is working -> {x}")
#     x+=1

# while x < 10:
#     print(f"it is working -> {x}")
#     if x == 4:
#         break
#     x+=1

# Verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age \n")
    if age.isdigit() and int(age) < 117 and int(age)!=0:
        user_prompt = False

    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age}")