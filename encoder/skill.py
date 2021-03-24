#!/usr/bin/python3

class Skill:
    name = ""
    id = -1
    w = 0.0
    l = []

	# parameterized constructor 
    def __init__(self, name, id, w, l):
        self.name = name
        self.id = id
        self.w = w
        self.l = l

    def display(self): 
        print("c skill " + self.name+ ", id = " + str(self.id) + ", weight = " + str(self.w) + ", agents = " + str(self.l)) 

    def display(self, outputFile):
        print("c skill " + self.name+ ", id = " + str(self.id) + ", weight = " + str(self.w) + ", agents = " + str(self.l), file=outputFile) 
