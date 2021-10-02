from os import system, name
from time import sleep

# Defining main() requires to make the program start and for the player to come back to the input screen when range is too small or too big. 
def main():
    
    # input
    x = int
    y = int

    x = input("Type number: ")
    y = input("Type another number to add with the previous number: ")

    # clear (only Windows, needs to have NT kernel)
    if name == 'nt':
        _ = system('cls')
  
    # clear (only macOS and Linux)
    else:
        _ = system('clear')

    # use an empty list
    numbers = []

    # add the specified numbers to the end of the list
    numbers.append(x)
    numbers.append(y)

    # [optional] printing the list with the added numbers inside
    # print(numbers)
    # print("")

    # checking the numbers you entered
    print("The first number you entered:", numbers[0])
    print("The second number you entered:", numbers[1])
    sleep(1)
    print("")

    # adding two numbers in a list
    # When these numbers are in a list, the first number is index 0, while the second is index 1. So use int (not sum)
    # to add the numbers with the varible 'numbers' with the index ([x]).
    result = int(numbers[0]) + int(numbers[1])

    # the combined sum
    print("Result:", result)
    print("")

    # The number has to be in the 20-50 range, otherwise less or greater than these numbers as shown will comeback to the input screen.
    # When OK, the program exits.
    if result < 20:
        print("Your result number is less than 20, therefore, your number is too small. Please try again with another result.")
        print("")
        main()
    elif result > 50:
        print("Your result number is greater than 50, therefore, your number is too big. Please try again with another result.")
        print("")
        main()
    else:
        print("Your result number is between the 20-50 range. OK.")

# The command to start the program to the main() function.
main()