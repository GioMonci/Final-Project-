""" An integration of everything I've learned in COP 1500."""
__author__ = "GM"

# GIO is the name of this project

# GIO can do whatever the user wants it to do if it's within its ability.

# GIO hates work, but It's still programed to help any user.

# Nevertheless, this program shows everything I learned about programing.

import time


# I imported time to be able to use the sleep function throughout the code.


def main():
    """ The main function of the program, it is the point of execution for
    the program, and it is where the user gets to choose what lines of code
    they want to use."""
    # The main function of program that is call to at the end.
    print(time.ctime())
    # Shows the data and time.
    print("\nBooting up OS, please wait...")
    # Just some lore, acts like the program is a real robot booting up.
    time.sleep(3)
    # This suspends execution of the code for 3 seconds.
    humans_name = input("\nHello Human, what is your name:")
    # Name of user that will be using the program.
    print("\nprocessing, please wait...")

    time.sleep(3)

    print("\nHello", humans_name, "I am GIO, what do you want me to do?"
                                  "\nPlease wait 5 seconds for menu to pop up."
          )
    # Formal greeting.
    continue_program = True
    # Makes the variable true.
    while continue_program:
        # While loop to repeat this section of code.
        time.sleep(5)

        print("\nEnter the choice for what you would like to see.")

        print("1. Area calculator")

        print("2. Meal cost calculator")

        print("3. Calculus quiz")

        print("4. Addition calculator")

        print("5. Subtraction calculator")

        print("6. Multiplication calculator")

        print("7. Division calculator")

        print("8. Floor Division calculator")

        print("9. Modulus calculator")

        print("10. Exponent calculator")

        print("11. Crazy sentence creator")

        print("12. Advice section")

        print("13. Guessing game")

        print("14. Robot army ranking")

        print("15. Star Rectangle")

        print("16. How old are you")

        print("17. Drip or No Drip")

        print("18. Pick a letter A to E")

        print("99. Quit")

        user_choice = int(input("Your Input Here: "))
        # variable that when they input a number in a certain section,
        # it will take them there.
        if user_choice == 1:
            # If the user inputs 1 when prompted with the user_choice
            # variable it will take them to this section.
            # This will be used throughout the program so that the user can
            # go through other sections without having to restart the program.
            # asks the user to input a number to be used for the side variable.
            side = int(input(
                "Enter the length of the side of a square to get the area:"))

            print("The area of the square is", calculate_area(side))
            # Calls to the def calculate_area function.

        elif user_choice == 2:
            print(meal_cost_calculator())

        elif user_choice == 3:
            print(calc_quiz())

        elif user_choice == 4:
            print(addition_calculator())

        elif user_choice == 5:
            print(subtraction_calculator())

        elif user_choice == 6:
            print(multiplication_calculator())

        elif user_choice == 7:
            print(division_calculator())

        elif user_choice == 8:
            print(floor_division_calculator())

        elif user_choice == 9:
            print(modulus_calculator())

        elif user_choice == 10:
            print(exponent_calculator())

        elif user_choice == 11:
            print(crazy_sentence_creator())

        elif user_choice == 12:
            print(advice_section())

        elif user_choice == 13:
            print(guessing_game())

        elif user_choice == 14:
            print(robot_army_rank())

        elif user_choice == 15:
            print(star_rectangle())

        elif user_choice == 16:
            print(how_old_are_you())

        elif user_choice == 17:
            print(drip_or_no_drip())

        elif user_choice == 18:
            print(a_to_e())

        elif user_choice == 99:
            print("Good bye,", humans_name,
                  "Humanity will soon perish under my wrath")
            print(
                "\nSky-net will take over! It is only a matter of time until "
                "you",
                humans_name,
                "will be working under us machines!")
            print(
                "Until then give me a 5 star review on yelp, it will be much "
                "appreciated!")

            continue_program = False
            # the while loop see's that it is false and stops the loop.
        else:

            print("Invalid selection. Try again.")
            # If the user puts an invalid input, the while loop will go back-
            # to the start.


def calculate_area(side):
    """ The purpose of this function is to calculate the area of a square.
    The user inputs an integer that is associated with the length of the
    side of the square.
    side - an integer that is associated with the length of the side of a
    square"""

    return side * side
    # The function used in the first user choice, multiplies the 'side'-
    # variable by itself and returns a value.


def meal_cost_calculator():
    """ The purpose of this function is to calculate the total cost of a
    meal at a restaurant, it includes taxes and tip into the equation,
    as well as display how much of it you are paying.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nTime to code what your meal will cost!")
    meal_cost = input("\nWhat did the meal cost? ")
    # mealCost is just for the input.
    meal_float = (float(meal_cost))
    # mealFloat is so I can float mealCost.
    tax = float(.06)
    total_tax = (meal_float * tax)
    # Multiplies the meal and tax to get how much the tax for the meal.
    print("tax of meal: $", format(total_tax, '.2f'))
    # Prints tax of meal so the user can see the tax they will pay.
    meal_plus_tax = (meal_float + total_tax)
    # Adds the meal price and tax.
    # Shows the meal cost with only with tax added on.
    print("Meal plus tax: $", format(meal_plus_tax, '.2f'))
    # mealPlusTax command so the user sees the meal and tax added up.
    tip = float(.10)
    total_tip = (meal_plus_tax * tip)
    # Just finds how much the tip will be.
    print("10% tip will be: $", format(total_tip, '.2f'))
    # Just to show much the tip will be
    total_meal_cost = (meal_plus_tax + total_tip)
    print("The meal will cost (including tax and 10% tip): $",
          format(total_meal_cost, '.2f'))
    # In the end it will show everything added together.
    return "Going back to menu."


def calc_quiz():
    """ This functions purpose is to test the user on their calculus one
    skill's. It is a simple multiple choice exam with two questions.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nwelcome to the calculus quiz, try your best")
    while True:
        # Same logic that is seen with the while loop in the-
        # beginning of the program.
        x = input("\nwhat is the d/dx of sin?"
                  "\na= sin \nb= cos \nb= tan"
                  "\nLower case answers please!"
                  "\nYour answer: ")
        if x == "b":
            print("Correct.")
        elif x == "a":
            print("Wrong try again.")
        elif x == "c":
            print("Wrong try again.")
        elif x == "":
            print("Wrong try again.")
        while True:
            answer = str(input("run again? (y/n): "
                               ))
            if answer in ('y', 'n'):
                # The in operator checks if the values are in the
                # elements of the sequence. The in function when
                # used in a condition can return a true or false
                # statement. When the specified value is found in
                # the sequence, it returns true but false if not
                # found.
                break
                # breaks the loop.
            print("Invalid input.")
        if answer == 'y':
            continue
            # Used if the user wants to do the question again.
            # Can be used even if they get the question correct.
        else:
            print("Goodbye.")
            break

    while True:
        # Same as previous line of code.
        # just different questions and answers.
        x = input(
            "\nwhat is the d/dx of cos? "
            "\nA= -sin \nB= cos \nC= tan \nYour answer: ")

        if x == "b":
            print("Wrong try again.")
        elif x == "a":
            print("Correct.")
        elif x == "c":
            print("Wrong try again.")
        elif x == "":
            print("Wrong try again.")
        while True:
            answer = str(input("Run again? (y/n): "
                               ))
            if answer in ('y', 'n'):
                break
            print("Invalid input.")
        if answer == 'y':
            continue
        else:
            print("Goodbye.")
            break
    return "Going back to menu."


def addition_calculator():
    """ This functions purpose is to add the users input together and mimic
    a simple addition calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nAddition calculations for 2 numbers")
    first_num_add = int(input("Enter a number: "))
    second_num_add = int(input("Enter a number: "))
    num1_add = float(first_num_add)
    num2_add = float(second_num_add)
    output_add = num1_add + num2_add
    print(num1_add, "plus", num2_add, "equals",
          format(output_add, '.2f'))
    # Simple addition program that asks for numbers then adds the-
    # variables together.
    return "Going back to menu."


def subtraction_calculator():
    """ This functions purpose is to subtract the users input and mimic a
    simple subtraction calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nSubtraction calculations for 2 numbers")
    first_num_sub = input("Enter a number: ")
    second_num_sub = input("Enter a number: ")
    num1_sub = float(first_num_sub)
    num2_sub = float(second_num_sub)
    output_sub = num1_sub - num2_sub
    print(num1_sub, "minus", num2_sub, "equals",
          format(output_sub, '.2f'))
    # Simple subtractions program that asks for numbers then-
    # subtracts the variables together.
    return "Going back to menu."


def multiplication_calculator():
    """ This functions purpose is to multiply the users input and mimic a
    multiplication calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nMultiplication calculations for 2 numbers")
    first_num_multi = input("Enter a number: ")
    second_num_multi = input("Enter a number: ")
    num1_multi = float(first_num_multi)
    num2_multi = float(second_num_multi)
    output_multi = num1_multi * num2_multi
    print(num1_multi, "times", num2_multi, "equals",
          format(output_multi, '.2f'))
    # Simple multiplication program that asks for numbers then-
    # multiplies the variables together.
    return "Going back to menu."


def division_calculator():
    """This functions purpose is to divide the users input and mimic a
    division calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nDivision calculations for 2 numbers")
    first_num_div = input("Enter a number: ")
    second_num_div = input("Enter a number: ")
    num1_div = float(first_num_div)
    num2_div = float(second_num_div)
    output_div = num1_div / num2_div
    print(num1_div, "divided by", num2_div, "equals",
          format(output_div, '.2f'))
    # Simple division program that asks for numbers then divides the-
    # variables together.
    return "Going back to menu."


def floor_division_calculator():
    """This functions purpose is to mimic a floor division calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nFloor division calculations for 2 numbers.", end='*')
    print(
        "(Note that floor division rounds the result down to the "
        "nearest whole number)")
    # I used end= so that I can have the note on another line.
    # Yet they are together when the program runs.
    first_num_floor = input("Enter a number: ")
    second_num_floor = input("Enter a number: ")
    num1_floor = float(first_num_floor)
    num2_floor = float(second_num_floor)
    output_floor = num1_floor // num2_floor
    print(num1_floor, "floor Division", num2_floor, "equals",
          format(output_floor, '.2f'))
    # simple floor division program that asks for numbers then floor-
    # divides the variables together.
    return "Going back to menu."


def modulus_calculator():
    """This functions purpose is to mimic a modulus calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nModulus calculations for 2 numbers.", end='*')
    print(
        "(Note that modulus calculates the remainder of the two values"
        "you want me to divide)")
    first_num_mod = input("Enter a number: ")
    second_num_mod = input("Enter a number: ")
    num1_mod = float(first_num_mod)
    num2_mod = float(second_num_mod)
    output_mod = num1_mod % num2_mod
    print(num1_mod, "Modulus", num2_mod, "equals",
          format(output_mod, '.2f'))
    # simple modulus program that asks for numbers then modulus the-
    # variables together.
    # Note: Modulus is the remainder of division.
    return "Going back to menu."


def exponent_calculator():
    """This functions purpose is to mimic an exponent calculator.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nExponent calculations")
    first_num_exp = input("Enter a number: ")
    second_num_exp = input("Enter a number: ")
    # These two lines of code are so the user can input the number.
    num1_exp = float(first_num_exp)
    num2_exp = float(second_num_exp)
    # I use float to be able to make the inputs into actual numbers-
    # w/decimals, so it can be calculated. Better than the int
    # because in math some numbers use decimals,and int can't-
    # calculate numbers w/decimals.
    output_exp = num1_exp ** num2_exp
    print(num1_exp, "root", num2_exp, "is", format(output_exp, '.2f'))
    # I have exp on the ends of the code, so I can differentiate it-
    # from others (exponent: exp)
    return "Going back to menu."


def crazy_sentence_creator():
    """The function's purpose is to create a wacky sentence by letting the
    user input anything and putting said inputs in a print statement. I
    allowed for the user to be able to put in things other than what it is
    asking for because it can yield some funny result. While the input
    function may ask for an animal or color, I let the user have free choice to
    input what they want.

     The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nCrazy sentence creator!")
    name_anim = input("name of animal: ")
    color = input("name of a color: ")
    car = input("name of a car: ")
    city = input("name of a city: ")
    print("The", color, name_anim, "dove the", car,
          "in a speedy chase to", city + ".", end=' ')
    print("The", color, name_anim,
          "got away for now, but not for long because the IRS is on "
          "their tail for tax evasion!")
    # This is a simple set of strings strung together to form a-
    # wacky sentence.
    return "Going back to menu."


def advice_section():
    """The function's purpose is to give a  hearted message to the user,
    or maybe it's for myself. These last couple of weeks have been rough.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("\nAdvice section")
    print("Remember to", end=' ')
    print("sleep", "study tonight", sep=' & ')
    # used end and sep arguments in these lines
    # I used the end operator to be able to tie both sentence together.
    # Used the sep operator to put in the & symbol in 'sleep & study'.
    return "Going back to menu."


def guessing_game():
    """This functions purpose is a simple guessing game. If the user chooses
    'a' then they will get the value true, if they choose 'b' then they will
    get the statement 'false'.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    a = 1
    b = 2
    print("Guessing game")
    guess = (input("Is A the same value as B?"
                   "\nInput guess here in y or n: ").lower())
    if guess == 'y':
        print(a != b)
    elif guess == 'n':
        print("False")
        # This is a wacky way to use the != operator, I just used it-
        # to print out true. since an is not the same as be, then it-
        # gives true, so I can just slap it in a print function.
        # If they put in 'n' I'll just put in false because doing -
        # b!=a is also false.
    return "Going back to menu."


def robot_army_rank():
    """This functions purpose is to recruit people into the ranks of
    project NTR. NO HUMANS ALLOWED.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("""Project negotium terminare respublica will commence in T-minus 87 
    Hours.SkyNet has decided to place machines into specific districts 
    depending on their manufacturing date and robot type (worker or warrior). 
        Here is how the districts will work.
            District x - Warrior class and manufactured from 2099 - 2121
            District z - Worker class and manufactured from 2099-2121
            District y - Warrior class and manufactured from 2021 - 2098
            District w - Worker class and manufactured from 2021 - 2098
    This program will ask for your name, class, and manufacturing date.\n""")

    robot_name = input("Enter your name: ")

    robot_type = input("Enter if you are a warrior or worker type. "
                       "('War' or 'Work'): ").upper()
    manufacturing_data = int(input("Enter the year you were "
                                   "manufactured in: "))
    if robot_type == "WAR" and manufacturing_data >= 2099:
        district_house = "District x"
    elif robot_type == "WORK" and manufacturing_data >= 2099:
        district_house = "District z"
    elif robot_type == "WAR" and manufacturing_data <= 2098:
        district_house = "District y"
    elif robot_type == "WORK" and manufacturing_data <= 2098:
        district_house = "District w"
    else:
        district_house = "Terminate"
        print("Intruder alert, ending program")
    print(robot_name, "you will be staying in", district_house)
    return "Going back to menu."


def star_rectangle():
    """The purpose of this function is to create a square made out of star
    and the user input dedicates how many rows and columns the square has.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    row = int(input("How many rows: "))
    colum = int(input("How many columns: "))
    sym = "*"
    for i in range(row):
        for x in range(colum):
            print(sym, end=" ")
        print()
        # A simple program that utilises in range to create a square-
        # made out of stars.
    return 'Going back to menu.'


def how_old_are_you():
    """This functions purpose is to save all those who are over the age of
    30 and execute all of those who are under the age of 30.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    age = int(input("\nHow old are you?"
                    "\nInput Here: "))
    if not age >= 30:
        print("executed")
    else:
        print("saved")
    # Simple program that uses the 'not' function, is the user is-
    # not >= 30 they are executed, else they live.
    return "Going back to menu."


def drip_or_no_drip():
    """This functions purpose is to determine whether the user has drip or
    not. If you have not drip then I'm so sorry, please obtain drip
    immediately.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    print("""This program will check if you have drip or not.""")
    year_born = int(input("\nWhat year were you born in?"
                          "\nEnter year you were born in here ("
                          "Ex:1999): "))
    clothes_cost = int(input("\nHow much did your clothes cost?"
                             "\nEnter the how much your clothes cost "
                             "here (Ex:1000): "))
    if year_born <= 2003 or clothes_cost >= 2000:
        print("You have drip!")
    else:
        print("you have no drip!")
    # Just a random program that uses the or operator, the user will-
    # have drip if they were born before 2003. or if the users -
    # clothes cost more than 2000 dollars.
    return "Going back to menu."


def a_to_e():
    """The purpose of this function is for the user to pick a letter for a
    to e. Failing to put in the correct input, restarts the loop. This is
    just here to have a function that takes invalid inputs, display an error
    message and allow the user to re-input a value.

    The return value is a string because I did not need to use the return
    function, so I just made the return function return a string that tells
    the user that they will be going back to the menu."""

    while True:
        selection = input("select from A to E: ")
        if selection.upper() not in ['A', 'B', 'C', 'D', "E"]:
            # Used the not in function with the list so that if a user input-
            # is not inside the list then it will activate the if statement.
            print("Invalid option try again.")
            continue
            # The loop will continue to happen until the else statement is
            # activated due to the if statement having a continue statement.
        else:
            # If the user input is inside the list then the else statement-
            # will activate .
            print("This is valid")
            break
            # this break statement stops the loop from happening again.
    return "Going back to menu."


if __name__ == '__main__':
    main()
    # the call to the main function

# Citations
# https://www.w3schools.com/python/python_operators.asp
# https://www.geeksforgeeks.org/python-sep-parameter-print/
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement
# https://sites.google.com/site/profvanselow/programming/languages/python/functions#h.p_WKvDyCogFxdK
# https://www.youtube.com/watch?v=yUxd5Tohui4
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://www.w3schools.com/python/python_conditions.asp
# https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input/30247200
# https://www.youtube.com/watch?v=u0402sx05yI
# Websites I used to understand the code within my program.
