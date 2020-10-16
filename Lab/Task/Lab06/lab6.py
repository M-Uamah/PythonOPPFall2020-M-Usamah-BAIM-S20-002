'''
create a clsss "fruit" with two variable "name" and "color" and a function "introduceFruit" and a constructor
which takes name and color as a peramiter
--> Create two class "winterFruit" and "summerFruit" both of these classes will contain a new function "fruitTaste" and a function introduce that override
the method of the parent class using inheritance.
--> Now crate 1 simple fruit and two summer and winter fruits.
'''
class fruit:
    fruitName = ""
    fruitColor = ""
    def __init__(self, name, color):
        self.fruitName = name
        self.fruitColor = color
    def introduce(self):
        print("Name of the fruit is " + self.fruitName)
        print("Color of the fruit is " + self.fruitColor)
        print ("It is a simple fruit")

class summerFurit(fruit):
    summerTaste = ""
    def __init__(self, name, color, taste):
        self.fruitName =  name
        self.fruitColor = name
        self.summerTaste = taste
    def taste(self):
        print("Taste of the fruit is "+ self.summerTaste)   
    def introduce(self):
        print("Name of the fruit is " + self.fruitName)
        print("Color of the fruit is " + self.fruitColor)
        print ("It is a summer fruit")
    
class winterFurit(fruit):
    winterTaste = ""
    def __init__(self, name, color, taste):
        self.fruitName =  name
        self.fruitColor = name
        self.winterTaste = taste
    def taste(self):
        print("Taste of the fruit is "+ self.winterTaste)
    def introduce(self):
        print("Name of the fruit is " + self.fruitName)
        print("Color of the fruit is " + self.fruitColor)
        print ("It is a winter fruit")
    


f1 = fruit("apple","green")
f1.introduce()

summer1 = summerFurit("manago", "yellow", "sweet")
summer1.taste()
summer1.introduce()

winter1 = winterFurit("Pears","green","sweet" )
winter1.taste()
winter1.introduce()
#to check it is working
print("code works")