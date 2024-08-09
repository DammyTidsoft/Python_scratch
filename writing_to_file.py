#writing into the file
#employee_file = open("employee.txt", "a")
employee_file = open("employee.txt", "w")
#using a "w" will overwrite the existing text in the file
#You can also use "w" to create a new file
#e.g
#employee_file = open("employee1.txt", "w")
#You can also create any other file
#e.g employee_file = open("employee.html", "w")
#print(employee_file.read())
employee_file.write("Tobi-->Humanitarian")
employee_file.write("\n Tolu-->Banker")
employee_file.close()