'''fl
A cat class!
'''
class Cat:
    def __init__(self, name):
        self.name = name
        self.will_purr = False
    def meow(self):
        print("meow")

david = Cat("David")

print("")

print("Hello and congratulations, you have won a free cat! What is your name? \n")

name = str(input())
print("")
print("Hello " + name + ". Do you like cats? (y/n)\n")

likes_cats = input()
print("")

if likes_cats == 'y':
    david.will_purr = True

print("Excellent choice. Would you like to pet the cat? (y/n)\n")

choice = input()
print("")

if david.will_purr:
    print(david.name + " the cat purred. David is very happy, " + name + ". \n")
else:
    print(david.name + " the cat said " + david.meow + ". He likes you, " + name + ".\n")

