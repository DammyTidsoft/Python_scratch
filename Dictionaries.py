#learning about dictionaries in python
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "SEptember",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
#in order to print any of the values in the dictionary
print(monthConversions["Nov"])
#you can also use this method for printing the value of the distionary
print(monthConversions.get("Dec"))