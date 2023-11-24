
# Define a function to calculate the sum of two numbers
def calculate():
    # Creating a list to store the calculations
    calculate = []
    # A variable to store the user input
    firstNumber = None

    # Loop through until the user enters "q"
    while firstNumber != "q":
        firstNumber = input("Enter first number: ")
        # Checking if the user enters "q"
        if firstNumber == "q":
            # Break the loop
            break
        # Try block to conver the first number to a int
        try:
            firstNumber = int(firstNumber)
        # If it fails then print the error message and continue the loop
        except ValueError:
            print("Invalid input. Please enter a number or q to quit.")
            continue
        # Prompt to let the user enter the second number
        secondNumber = input("Enter second number: ")
        # Try block to conver the second number to a int
        try:
            secondNumber = int(secondNumber)
        except ValueError:
            print("Invalid input. Please enter a number or q to quit.")
            continue
        # Result of the two numbers
        result = firstNumber + secondNumber
        # Printing the result
        print(f"{firstNumber} + {secondNumber} = {result}")

        # Append the calculation to the list
        calculate.append(f"{firstNumber} + {secondNumber} = {result}")


def ex4():
    calculate()

ex4()
