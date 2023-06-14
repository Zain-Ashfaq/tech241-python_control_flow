# for and while loops

# in python we just use for

list_data = [1,2,3,4,5]
embedded_lists = [[1,2,3], [4,5,6]]

dict_data = {
    1: {"name": "Bronson", "money":"$0.05"},
    2: {"name": "Masha", "money":"$3.36"},
    3: {"name": "Roscoe", "money":"$1.14"},
}

# for num in list_data:
#     print(num)

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

for item in dict_data.values():
    print(item)
    for embed_value, test in item.items():
        print(embed_value,test)

# a loop that only returns money

for items in dict_data.values():
    print(items["money"])


# loops and if statements

for num in list_data:
    if num == 3:
        print("You have found three!")

    elif num > 3:
        print("Gone too far")
    else:
        print("too soon")