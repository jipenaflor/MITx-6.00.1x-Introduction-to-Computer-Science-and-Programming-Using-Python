"""Implement a class so that the following ArrogantProfessor behavior is achieved:
    ae = ArrogantProfessor('eric')
    ae.say('the sky is blue')
        eric says: It is obvious that eric says: the sky is blue
    ae.lecture('the sky is blue')
        It is obvious that eric says: the sky is blue
"""

#Given code:
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

#Problem 6:
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+'It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff
        
