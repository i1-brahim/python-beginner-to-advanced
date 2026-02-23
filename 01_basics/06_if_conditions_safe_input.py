user_input = input("Enter A Number: ")


try:

    user_input = user_input.replace(",", ".")

    number = float(user_input)
                                    
    if number > 0:
        result = "This Number Is Positive. "

    elif number < 0:
        result = "This Number Is Negative. "

    else:
        result = "This Is Zero. "

    print(result)

except ValueError:
    print("Invalid input. Please enter a valid numeric value. ")
    
