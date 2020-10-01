class animal:
    name = ""
    color = ""
    def introduceAnimal(self):
        print("The name of the is " + self.name,"\nThe color is " +self.color)
    def speakAnimal(self,speak):
        print(self.name + " makes "+ speak)

class landAnimal(animal):
    def walk(self):
        print(self.name + " can walk")
class seaAnimal(animal):
    def swim(self):
        print(self.name + " can swim")
''''
#testing the function
ani = animal()
ani.name = "dog"
ani.color = "black"
ani.introduceAnimal
ani.speakAnimal("wao wao")
'''
ani1 = landAnimal()
ani1.name = "dog"
ani1.color = "black"
ani1.speakAnimal("bark")
ani1.walk()

ani2 = landAnimal()
ani2.name = "cat"
ani2.color = "white"
ani2.speakAnimal("mewo")
ani2.walk()

ani3 = seaAnimal()
ani3.name = "shark"
ani3.color = "white"
ani3.speakAnimal("no sound")
ani3.swim()

ani4 = seaAnimal()
ani4.name = "Wale"
ani4.color = "black"
ani4.speakAnimal("Donsl Philippines")
ani4.swim()

#for testig the code works or not
# print("Working")