# https://trello.com/c/oQjNZjQz/64-control-flow-task-1-improved-movie-ratings-program

def check_age(input_age):
    if input_age >= 18:
        print("You can watch all movies.")
    elif input_age >= 15:
        print("You can watch 15 and lower rated movies.")
    elif input_age >= 12:
        print("You can watch 12 and lower rated movies.")
    elif input_age >= 8:
        print("You can only watch U-rated movies.")
    else:
        print("You can only watch U-rated movies.")

is_user_age_valid = False

while not is_user_age_valid:
    age = input("Enter your age: ")

    if age.isdigit() and 0 < int(age) <= 117:
        check_age(int(age))
        is_user_age_valid = True
    else:
        print("Please enter a valid age between 1 and 117.")
