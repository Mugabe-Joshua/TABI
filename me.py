my_name = input("What is your name? ").title()
print(f"Hello, {my_name}!")


# #DATA TYPES
# # Strings
# "5"

# # Integers
# 5

# # Floats
# 5.2

# # Booleans
# True
# False

# is_female = input("Are you female? ").title().strip()
# while is_female == "Yes":
#     print(f"Hello, Ms. {my_name}!")
#     if is_female == "No":
#         print(f"Hello, Mr. {my_name}!")
#     else:
#         print(f"Please select your gender before continuing {my_name}!")
#     break

while True:
    is_female = input("Are you female? (Yes/No) ").title().strip()
    if is_female == "Yes":
            print(f"Hello, Ms. {my_name}!")
    elif is_female == "No":
            print(f"Hello, Mr. {my_name}!")
    else:
        print(f"Please select your gender before continuing, {my_name}!")
        break
    break    

