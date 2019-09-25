# Fucntions
def make_dough(arg1,arg2):
    if (arg1 == 'water' and arg2 == 'wheat') or (arg1 == 'wheat' or arg2 == 'water'):
        return 'dough'
    elif (arg1 == 'sand' and arg2 == 'cemet') or ( arg1 == 'cemet' and arg2 == 'sand'):
        return 'not dough'

def wood_oven(arg1):
    if arg1 == 'dough':
        return 'Naan bread'
# Calling of functions




# Tests TDD
print("Testing make dough, with wheat and water --> dought to come out")
print(make_dough('water','wheat') == 'dough')


print("Testing make_dough, witht 'sand and 'cement' --> to come out ")
print(make_dough('sand','cement') == 'Not dough')


print("Testing wood_over with dough --> nan bread to come out")
print(wood_oven('dough') == 'Naan bread')





