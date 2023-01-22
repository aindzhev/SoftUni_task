def intro():
    return '''#################################
#  Welcome to my calculator     #
#  Please select an option      #
#        to continue            #
#                               #
#                               #
#  Author:Antonio Indzhev       #
#  Course:SoftUni Fundamentals  #
#                               #
#################################/n'''


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print(intro())

while True:
    choice = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nEnter your choice:"))

    if choice == 5 or choice > 5:
        print("Thank you for using my calculator")
        break

    n1 = float(input("Enter first number:"))
    n2 = float(input("Enter second number:"))

    if choice == 1:
        print("Total:", add(n1, n2))
    elif choice == 2:
        print("Total:", subtract(n1, n2))
    elif choice == 3:
        print("Total:", multiply(n1, n2))
    elif choice == 4:
        print("Total:", divide(n1, n2))
