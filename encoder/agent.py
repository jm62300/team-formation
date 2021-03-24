#!/usr/bin/python3

class Agent:
    name = ""
    id = -1
    w1 = 0.0
    w2 = 0.0
    l = []

	# parameterized constructor 
    def __init__(self, name, id, w1, w2, l):
        self.name = name
        self.id = id
        self.w1 = w1
        self.w2 = w2 
        self.l = l

    def display(self): 
        print("c agent " + str(self.name) + ", id =  " + str(self.id) + ", weight phase 1 = " + str(self.w1) +
              ", weight phase 2 = " + str(self.w2) + ", skills = " + str(self.l)) 

    def display(self, outputFile):
        print("c agent " + str(self.name) + ", id =  " + str(self.id) + ", weight phase 1 = " + str(self.w1) +
              ", weight phase 2 = " + str(self.w2) + ", skills = " + str(self.l), file=outputFile) 
