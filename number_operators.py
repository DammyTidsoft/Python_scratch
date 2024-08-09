#working with numbers
'''
firstname="Abdul Qayyum"
lastname="Balogun"
age = "15"
address="Ifo"
myclass ="SS 1"
print("My first name is: "+ firstname)
print("My surname is: "+ lastname)
print("I am"+age + "years old")
print("I am living in:"+address)
print("I am in: "+ myclass)
'''
'''
firstname = input("What is your name?: ")
lastname = input("What is your surname?:")
age=input("How old are you?:")
address=input("Where are you living?:")
myclass =input("what class are you?:")
print("Your name is: "+lastname+""+firstname)
print("You are "+age+"years old")
print("You live in"+address)
print("You are in: "+myclass)
'''

'''
lenght=input("Enter the value of lenght:")
breadth=input("Enter the value of breadth:")
perimeter = int(lenght) * int(breadth)
print("This is the perimeter value: " , perimeter)
'''

#calculating the simple interest
p=input("Enter the value of principal: " )
t = input("Enter the value of time: ")
r = input("Enter the value of rate: ")
simple_interest = (int(p) * int(t) * int(r))/100
print("The simple interest is: " , simple_interest)
