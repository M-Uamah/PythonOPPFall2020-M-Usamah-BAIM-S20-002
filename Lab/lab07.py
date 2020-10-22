#Operator Overloading
'''
--> Benfit
--> how to do it
--> where to do it
--> how it works
'''

"""
--> Benifit

"""
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
    def __add__(self, hello):
        temp = self.fruitName + " " + hello.fruitName
        return temp
        # pass

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
f2 = fruit("bary", "blue")
f3 = fruit("strobry", "red") 
f3 = f2 + f1
# f3.introduce()
print(f3)

# summer1 = summerFurit("manago", "yellow", "sweet")
# summer1.taste()
# summer1.introduce()

# winter1 = winterFurit("Pears","green","sweet" )
# winter1.taste()
# winter1.introduce()
# #to check it is working
# print("code works")
'''

class vehicle:
    no_of_wheel = ""
    no_of_lights = ""

    def indrotuceVehicle(self):
        print("I am a simple vehicle with " + self.no_of_wheel + " wheel\n" +"I have " + self.no_of_lights + " lights"  )

    def __add__(self, other):
        temp1 = self.no_of_lights + other.no_of_lights
        temp2 = self.no_of_wheel + other.no_of_wheel
        return [temp1, temp2]

trackters = vehicle()
trackters.no_of_lights =4 
trackters.no_of_wheel = 4

trali = vehicle()
trali.no_of_wheel = 2
trali.no_of_lights = 2

trackterstrali = vehicle()
trackterstrali = trackters + trali
print(trackterstrali)