# author: <Samaiya Howard>
# date: <7/2/21>
#
# description: <Vairables practice page 1>

# --------------- Section 1 --------------- #

# 1.1 | Variable Creation | Strings
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that holds your name.
#   2) Create a variable that holds your birthday.
#   3) Create a variable that holds the name of an animal you like.
#
# Print
#   4) Print each variable, describing it when you print it.
#
# Example Code
example_name = 'elia'
print('EXAMPLE: my name is', example_name)

# WRITE CODE BELOW
name = "Samaiya Howard"
birthday = "August 25"
animal = "lion"
print("My name is:", name + "\n" +"My birthday is:",birthday + "\n" +"and the animal I like is:", animal)


# 1.2 | Variable Creation | Integers / Floats
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# All variables created in this section should hold either an integer or float.
#
# Variables
#   1) Create a variable that holds your favorite number.
#   2) Create a variable that holds the day of the month of your birthday.
#   3) Create a variable that holds a negative number.
#   4) Create a variable that holds a floating (decimal) point number.
#
# Print
#   5) Print each variable, describing the value you print.

# WRITE CODE BELOW
print()
favNum = 4
birthday_monthDay = "thursday"
negNum = -256
decimalNum = 3.14159
print("My favorite number is:", favNum, "\n", "My birthday day is:",birthday_monthDay, "\n", "A negative number is:",negNum, "\n", "A decimal number is:",decimalNum)



# 1.3 | Overwriting Variables
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Overwrite the variable holding your name, and save a different name to it.
#   2) Overwrite the variable holding birthday with the day you think would be best to have a birthday on.
#   3) Overwrite the variable holding your favorite number and set it to a number you think is unlucky.
#
# Print
#   4) Print the variables you've overwritten, describing the values you print.
#
# Example Code
example_name = 'lucia'
print('EXAMPLE: my new name is', example_name)

# WRITE CODE BELOW
print()
myName = name
myBirthday = birthday
UnluckyNum = favNum
UnluckyNum = -6
print("My name is:",myName,"\n","My birthday is:",myBirthday,"\n","The number I think that is unlucky is:",UnluckyNum)


# 1.4 | Operations
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that is the sum of two numbers.
#   2) Create a variable that is the product of three numbers.
#   3) Create a variable by dividing the previously created sum, with the previously created product.
#
#   4) Create a variable that is the concatenation of your name and an animal you like (use the variables!)
#   5) Create a variable that is an acronym (like 'lol') multiplied by your birth day.
#
#   6) Create a variable that is difference of itself minus the number you think is unlucky.
#   7) Overwrite the lucky variable with the itself squared.
#
# Print
#   7) Print all the new variables you've created along with what the represent
#
# Example Code
example_sum = 11 + 21
print('EXAMPLE: the sum of 11 and 21 is', example_sum)

# WRITE CODE BELOW
sum1 = 1073 + 47
productOf3 = 20 + 17 + 67
sumProductdivided = sum1 / productOf3
nameandanimal = myName + animal
myacronym = "ttyl"*25
numSubtracted = 790 - 734
unlucksubtractnum = numSubtracted - UnluckyNum
luckynum = favNum ** favNum
print("the sum of 1073 and 47 is:",sum1,"\n","The product of 20, 17, and 67 is:",productOf3,"\n","The sum of 1073 & 47 divided by the product of 20,17 & 67 is:",sumProductdivided,"\n","The concatenation of my name and an animal I like is:",nameandanimal,"\n","One acronym I chose multiplied by my birthday is:", myacronym,"\n","A number difference subtracted by my unlucky number is:",unlucksubtractnum,"\n","My lucky num squared is:", luckynum)