#reading from external file in python
#You can use it to get information
#You can use a special command called open
#open("employee_file.txt", "r")
'''
You can read the file, delete, modify and add
"r" --> to read the content of the file
"r+"
As we have open file, we also have a close file
'''
employee_file = open("employee_file.txt", "r")

#print(employee_file.readable())
#print(employee_file.readlines())
for employee in employee_file.readlines():
    #print(employee_file.readlines()[2])
    print(employee)
employee_file.close()
