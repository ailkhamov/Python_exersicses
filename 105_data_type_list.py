# List
# List keep object in order of index
# It's defined by []

# list_name  =    [ 0 ,         1,      2            3  ]
crazy_x_partners = ['Carolina', 'JSON', 'Arthur', 'Lana!']

# print and show type
print(crazy_x_partners)
print(type(crazy_x_partners))

# Get a particular record out
# Lists are organised with index
print(crazy_x_partners[0]) #  use the index inside square brackets [i]

# How do i I print the last one?
print(crazy_x_partners[-1])

# How to change record in a list ?
crazy_x_partners[3] = 'Lana'

# How to add more poeple to the list (Create one) -append()
print(crazy_x_partners)
crazy_x_partners.append('Siral Figus')
print(crazy_x_partners)

# insert in index specific location
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)
# Remove someone from the list (Destroy one)
crazy_x_partners.remove('JSON')
print(crazy_x_partners)

# Remove using index
crazy_x_partners.pop()   # remove last entry
crazy_x_partners.pop(1)  # removes based on index
# Add more people to the list (Create one)

# Mixed data and LISt
# Lists can have many data types
hybrid_list = ['This is a string', 12, 66, 'Hello', [1,2,3], [1,2,2]]

# Tuples - Imutable lists - they do not change
# syntax
# my_tuple = ()

my_tuple = (2, "Hello", 22, 'More value')
print(my_tuple)
print(type(my_tuple))

#   # slicing
print(crazy_x_partners[:1]) # 0 to 1 not inclusive
print(crazy_x_partners[1:3]) # from 1 to 2, not inclusive of 2

# Jumping/Slicing
example_list = [0, 1, 2, 3, 5, 6, 7, 8, 9]
print(example_list[::2])