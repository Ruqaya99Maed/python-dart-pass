     
class Animal():
    def _init_(self, name, sound):
        self.name =  name
        self.sound = sound
    def printName(self):
        print (f'My name is {self.name}')
    def printSound (self): print (f'My sound is {self.sound}')

class Dog(Animal):
        def _init_(self, name, sound):
            self.name = name
            self.sound = sound

class Cat (Animal):
    def _init_(self, name, sound):
        self.name = name
        self.sound = sound

class Cow (Animal):
    def _init (self, name, sound):
        self.name = name
        self.sound = sound

dog1 = Dog("semo", "haw haw")

dog1.printSound()

dog1.printName()   
