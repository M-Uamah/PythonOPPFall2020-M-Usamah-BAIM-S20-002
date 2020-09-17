## Task 01
# Create two classes university and teacher

class university:
    uniName = ""
    uniCity = ""
    uniAge = ""

    def  universityInformation(self):
        print("--------------------------------------------------------------------")
        print("Name of the University is " + self.uniName)
        print("It is located in " + self.uniCity )
        print("It was created " + str(self.uniAge) + " old")
        print("--------------------------------------------------------------------")

uni1 = university()
uni1.uniName = "Superior"
uni1.uniCity = "Lahore"
uni1.uniAge = 40
uni1.universityInformation()

print("All is good")

