
# class Dog:
#     atr1 = "animal"
#     atr2 = "white"
#
#     def func(self):
#         print("Dog is a ", self.atr1)
#         print("Dog is a ", self.atr2)
#
#
# refVar = Dog()
# print("Abt to call function")
# refVar.func()
########### Constructor ##############
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def myOwnMethod(self):
#         print("My name is ", self.name)
#
# p = Person("Omkar")
# p.myOwnMethod()

########### instance variables ##################

class Dog:
    #class variables
    animal = "Cat"
    # create a constructor function
    def __init__(self, breed, color):
        print("inside the constructor function")
        #instance variable
        self.breed = breed
        self.color = color

s = Dog("Persion Cat", "White")
r = Dog("American", "Brown")

print("Object for s ", s.breed)
print("Object for s ", s.color)

print("Object for r ", r.breed)
print("Object for r ", r.color)
