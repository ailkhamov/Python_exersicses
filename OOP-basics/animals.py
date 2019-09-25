class Animal():

    # Charectersitics
    def __init__(self, name, eyes, eater, age): # runs only once when you initialize an object
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.number_animals_eater = eater
        self.age = age

    #Charecteristics
    # Behaviours - functions that belong to a class
    # Methods - functions that can only be used on this class instance

    def eat(self,food = ''): # making an argument optional # self - is an original object in which you call something
        return "NOM NOM NOM" + " "  + food

    def sleep(self):
        return "ZzzzZZZzzzZZZ Zzz slleeyy"

    def hunt(self):
        return 'ATTACCKKKKK THIS IS SPARTA'

    def potty(self):
        return '0_0 ....HUNN o_0 --- HUUUH!! O_O '




# Let's create an object of class Animal :)
    # Initializing an object

