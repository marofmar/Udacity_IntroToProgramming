class Dog:
    scientific_name = "cute"

    def do_trick(self):
        pass

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!") 


    def hear(self, words):
        if self.name in words:
            self.speak() 
            
    def eat(self, food):
        if food == 'buiscuit':
            print("Yummy!")
        if food == 'chair':
            print("That is not food!")

    def count(self):
        self.woofs+=1
        for bark in range(self.woofs):
            self.speak() 

def chihuahua(Dog):
    origina = "Mexico"

    def speak(self):
        print("Yip!")

def TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The chihuahua spins in the air and turns briefly into a chicken.")

def Husty(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoooooooo")

class Cat:

    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purrr")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")