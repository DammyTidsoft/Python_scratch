#function are collection of code which perform a specific task
def say_hi():
    print("hello")
say_hi()
#function that has parameters
def working_function(name,age):
    print("hello"+ ""+name + ""+ "you are"+""+age)
working_function("steve","21")
working_function("Damilare","43")
working_function("Demilade", "35")
#integer functions
def lucky_figures(age,lucky_number):
    print("Your age is "+ str(age) + ", and your lucky number is " +str(lucky_number))
lucky_figures(20,39)
#python functions return statement
def cube(num):
    return num*num*num
print(cube(4))