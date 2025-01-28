my_name = input("What is your name? ").title()
print(f"Hello, {my_name}!")


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

