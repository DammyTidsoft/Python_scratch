#working with list in python
friends = ["Deborah","Bunmi","Busayo","Damilare","Dimeji"]
lucky_numbers = [1,3,6,4,9,3,2]
#list modification
friends[2] = "Tomiwa"
print("My friends are:"+"")
print(friends[0:3])
#list functions
#extend function
friends.extend(lucky_numbers)
print(friends)
#append function
friends.append("Creed")
print (friends)
#insert function
friends.insert(1,"Demilade")
print(friends)
#remove function
friends.remove("Demilade")
print(friends)
#clear function
lucky_numbers.clear()
print(friends)
#pop function
friends.pop()
print(friends)
#index function
print(friends.index("Damilare"))
#count function
print(friends.count("Bunmi"))
#sort function
prime_numbers =[19,2,3,5,7,11,13,17]
prime_numbers.sort()
print(prime_numbers)
#reverse function
prime_numbers.reverse()
print(prime_numbers)
#copy function
hobby =["reading","singing","writing"]
likeness = hobby.copy()
print(likeness)