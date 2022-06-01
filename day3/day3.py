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