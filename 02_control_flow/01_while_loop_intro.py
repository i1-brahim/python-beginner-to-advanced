# 01_while_loop_intro.py
# Control Flow - While Loop Introduction


while True:
    user_input = input("Enter A Number (Or Type 'q' To Quit): ")

    if user_input.lower() == "q":
        print("Program Terminated By User.")
        break

    try:
        user_input = user_input.replace(",", ".")
        number = float(user_input)

        if number > 0:
            print("The Number Is Positive.")

        elif number < 0:
            print("The Number Is Negative.")

        else:
            print("This Is Zero.")

    except ValueError:
        print("This is a string input. Output cannot be produced.")





