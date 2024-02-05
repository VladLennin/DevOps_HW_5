def __main__():
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    flag = True
    while flag:
        action = int(input("Choose action:\n 1.+ \n 2.- \n 3.* \n 4./")) - 1
        if action == 0:
            print(first_number + second_number)
        elif action == 1:
            print(first_number - second_number)
        elif action == 2:
            print(first_number * second_number)
        elif action == 3:
            print(first_number / second_number)
        else:
            print("Wrong action")
            continue
        flag = False


__main__()
