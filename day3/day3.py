#Write a program that works out whether if a given number is an odd or even number.

def even_or_odd():
    number = int(input("Which number do you want to check? "))
    if number % 2 == 0:
        print(f"This is an even number")
    else:
        print("This is an odd number")

#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

def bmi_indicator():
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    bmi = weight / height ** 2

    if bmi < 18.5:
        print(f"Your BMI is {round(bmi)}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {round(bmi)}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {round(bmi)}, you are obese.")
    else:
        print(f"Your BMI is {round(bmi)}, you are clinically obese")

#Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.

def leapYear():
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not Leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

def pizzaChanllenge():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")

    if size == "S":
        total = 15
        if add_pepperoni == "Y":
            total += 2
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
        else:
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
    elif size == "M":
        total = 20
        if add_pepperoni == "Y":
            total += 3
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
        else:
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
    elif size == "L":
        total = 25
        if add_pepperoni == "Y":
            total += 3
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
        else:
            if extra_cheese == "Y":
                total += 1
                print(f"Your final bill is: ${total}")
            else:
                print(f"Your final bill is: ${total}")
    else:
        print("Select a pizza size please")

def treasureIsland():
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure")
    print("You're on a cross road. Where do you want to go? Type " +'"left" or "right"')
    input1 = input()
    if input1 == "left":
        print("You come to a lake. There is an island in the middle of the lake. Type "+'"wait" to wait for a boat. Type "swim" to swim across.')
        input2 = input()
        if input2 == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
            input3 = input()
            if input3 == "red":
                print("Burned by fire")
                print("Game Over")
            elif input3 == "blue":
                print("Eaten by beasts.")
                print("Game Over.")
            elif input3 == "yellow":
                print("You Win!")
            else:
                print("Game Over")


        else:
            print("Attacked by tryout.")
            print("Game Over.")
    else:
        print("Fall into a hole.")
        print("Game Over.")
