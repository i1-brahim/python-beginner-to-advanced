counter = 0
max_attempts = 5

while True:
    user_input = input("Enter A Number Or 'q' To Quit: ")

    if user_input.lower() == 'q':
        print("Program Terminated By User.")
        break

    try:
        user_input = user_input.replace(",", ".")
        number = float(user_input)

    except  ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    counter += 1
    print("Attempt:", counter, "I Number Entered:", number)

    if counter >= max_attempts:
        print("Maximum number of attempts reached.")
        break

