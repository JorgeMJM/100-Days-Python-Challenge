#We need to print the next output

#Day 1 - Python Print Function
#The function is declared like this:
#print('what to print')

def exercise1():
    print("Day 1 - Python Print Function")
    print("The function is declared like this:")
    print("print('what to print)")

# On exercise2, we are asked to print the next text:
#Day 1 - String Manipulation
#String Concatenation is done with the "+" sign.
#e.g. print("Hello " + "world")
#New lines can be created with a backslash and n.
#So we are going to inserted in a function to print

def exercise2():
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")

#In this excersise we need to print the length of any name
def exercise3():
    name = input("What's your name?")
    print(len(name))

#Instructions
#Write a program that switches the values stored in the variables a and b.

#Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

#Example input
# a:3
# b:5

#Example Output
# a:5
# b:3

def exercise4():
    a = int(input("a: "))
    b = int(input("b: "))

    a = a + b
    b = a - b
    a = a - b

    print("")
    print(f"a: {a}")
    print(f"b: {b}")

# other way to do it is:
# aux1 = a
# aux2 = b
# a = aux2
# b = aux1
#This will work for the codingroom, but it is an inneficcient way to do it because it will take more mememory