class parent:
    fatherName = ""
    motherName = ""
    def motorcycle(self):
        print("This is " + str(self.fatherName) + " motorcylce")
    

class child(parent):
    childName = ""
    childAge = ""

parent1 = parent()
parent1.fatherName = "Murtaza"
parent1.motherName = "Sumara"
parent1.motorcycle()

child1 = child()
child1.childName = "Usamah"
child1.childAge = 20
child1.motorcycle()