
#_________________________________________Inheritance_________________________________________

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):                  # Inherited from class Animal
    def __init__(self):
        super().__init__()

    def breathe(self):               # function overriding
        super().breathe()
        print("Doing this underwater.")
        
    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)