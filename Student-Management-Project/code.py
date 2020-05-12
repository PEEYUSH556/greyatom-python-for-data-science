# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings

new_class = class_1 + class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list

print(new_class)
# Remove the element from the list
new_class.pop(5)
# Print the list

print(new_class)

# Create the Dictionary

courses = {'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60}

# Store the all the subject in one variable `Total`
Total = 65 + 70 + 80 + 70 + 60
# Print the total
print(Total)
# Insert percentage formula
percentage = (Total / len(courses)) * 100
# Print the percentage
print(percentage)

# Create the Dictionary
 
mathematics = {'Geoffrey Hinton': 78,
'Andrew Ng': 95,
'Sebastian Raschka': 65,
'Yoshua Benjio': 50,
'Hilary Mason':	70,
'Corinna Cortes': 66,
'Peter Warden':	75}

# Given string

topper = max(mathematics,key = mathematics.get)
print (topper)
# Create variable first_name 
print('-'*20)
first_name = topper.split()[0]
print(first_name)
# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]
print(last_name)
full_name = []
# Concatenate the string
full_name = first_name + ' ' + last_name
# print the full_name
print(full_name)
# print the name in upper case
full_name.upper()
print(full_name)
certificate_name = 'NG ANDREW'
print(certificate_name)
# Code ends here


