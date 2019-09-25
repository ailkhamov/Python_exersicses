
cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corbet']
 #Syntax

 # for <placeholder> in <iteratable>:
    # block of code
    # indented get run every iteration


for car in cars:
    print(car)

# Don't forget the column

embeded_list=[['abror', 'drogba'], ['rooney', 'pogba']]


student1 = {
    'name': 'Arya Stark',
    'stream': 'Man Faces',
    'grade': 10,
    'complete module': ['Sword','Agumented Error','no face']
}
student2= {
    'name': 'Abror Ilkhamov',
    'stream': 'Man Faces',
    'grade': 10,
    'complete module': ['Sword','Agumented Error','no face']
}
for key, values in student1.items():
    print(key,':',values)


students = {
    'Student1': student1,
    'Student2': { 'name': 'Olsi Berish',
    'stream': 'Python',
    'grade': 10,
    'complete module': ['Danger','Alive','Pogba']
}
}

counter = 1

for key in students:

    counter = 1
    for key1 in students[key]:

        print(f'{counter} {key1} : {students[key][key1]} ')
        counter+= 1

# While loops

