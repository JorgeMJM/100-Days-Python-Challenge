#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

def exercise1():
    two_digit_number = input("Type a two digit number: ")

    sum = int(two_digit_number[0]) + int(two_digit_number[1])
    print(sum)

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


def exercise2():
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    bmi = float(weight) / float(height) ** 2
    print(int(bmi))

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.
#Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

def exercise3():
    age = input("What is your current age?")
    until = 90
    x = until * 365 - int(age) * 365
    y = until * 52 - int(age) * 52
    z = until * 12 - int(age) * 12
    print(f"You have {x} days, {y} weeks, and {z} months left")

