# Write a python program to calculate the length of a string
print(len("Hello"))
# or
def string_length(string):
    count = 0
    for char in string:
        count +=1
    return count
print(string_length("Hello"))
# Write a program to sum all the items in  a list
list = [5,5,5]
print(sum(list))
# OR
def sum_list_total(list):
    sum_numbers = 0
    for x in list:
        sum_numbers+=1
    return sum_numbers
print(sum_list_total([2,5,10]))

# Write a python program to multipiles all the items in a list
def largest_number(items):
    total = items[0]
    for x in items:
        total *= x
    return total
print(largest_number([1,2,10]))
# Write a program to count the number of charectors in a string
golf = "Golf is great"
print(golf.count("golf"))

# write python program to get the last part of a
# string before specified character

# Reverse a string

def reverse_string(str1):
    return ''.join(reversed(str1))
print(reverse_string("abror ilhamov"))