#string is just an array of chars 

first_name = input('Enter first name: ')
last_name = input('Enter last name:')

#strings can be concatenated by '+' sign
full_name = first_name + last_name
print("Full name: " + first_name + " " + last_name)


#convert string to uppercase 
print(full_name.upper())

#print length of the string
print(len(full_name))

#check string if it contains "foo"
x = "foo" in full_name
print(x)
