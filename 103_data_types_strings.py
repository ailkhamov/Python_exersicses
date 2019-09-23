# Strings are a list of charectors put together and they are defined by '' or ""


my_string = 'Amazing Grilled Fish'
print(type(my_string))

## You can print it
print(my_string)

# Join of strings -concatenation

first_name =  'Abror'
last_name = 'Ilkhamov'

# Concatenation 3 strings
full_name = first_name + ' ' + last_name
print(full_name)

# Useful methods for strings
my_string = "  Hello this is an amazing string  "

# count()
print(my_string.count('i'))

# leng() - removes white spaces - not a method - general method built in
print(len(my_string))

# Strip()
print(my_string.strip())

# .lower()  - returns everything in lower cases

print(my_string.lower())
# .upper() = returns everything in upper cases
print(my_string.upper())
# .capitalize
print(my_string.strip().capitalize())

# .replace(arg int, arg two)
print(my_string.replace('an', 'The'))

# .split(arg) --> List
print(my_string.split(' '))
# Interpolation
name  = 'Rachel'
print(f'Hey there, {name} how you doing')