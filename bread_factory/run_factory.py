# Fucntions
def make_dough(ingridient1, ingridient2):
    if (ingridient1 == 'water' and ingridient2 == 'wheat') or (ingridient1 == 'wheat' or ingridient2 == 'water'):
        return 'dough'
    else:
        return 'Not dough'

def wood_oven(arg1):
    if arg1 == 'dough':
        return 'Naan bread'
def run_naan_factory(ingrediant1, ingridiant2):
    # needs to amek dough
    dough_r = make_dough(ingrediant1,ingridiant2)
    result_bread = wood_oven(dough_r)

    return result_bread

print(run_naan_factory("wheat",'water'))
# Calling of functions




# Tests TDD
print("Testing make dough, with wheat and water --> dought to come out")
print(make_dough('water','wheat') == 'dough')


print("Testing make_dough, witht 'sand and 'cement' --> not to come out ")
print(make_dough('sand','cemet') == 'Not dough')


print("Testing wood_over with dough --> nan bread to come out")
print(wood_oven('dough') == 'Naan bread')





