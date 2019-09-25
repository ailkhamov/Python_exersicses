from nunf_functions import *

# Tests TDD
print("Testing make dough, with wheat and water --> dought to come out")
print(make_dough('water','wheat') == 'dough')


print("Testing make_dough, witht 'sand and 'cement' --> not to come out ")
print(make_dough('sand','cemet') == 'Not dough')


print("Testing wood_over with dough --> nan bread to come out")
print(wood_oven('dough') == 'Naan bread')


