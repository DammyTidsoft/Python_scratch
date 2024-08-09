'''
This is how to use try and except for running a convenient program in p
python, it is very good for our python program
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

'''
their are many exceptions in pythong
it include 
ZeroDivisionError
ValueError
etc
'''
#Example
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second "))
    result = int(number1 * number1)
    print(result)
except:
    print("Please Enter Numbers")