## Task 01
# Create two classes university and teacher

print("=====================================================================")
print("                                Task 01                              ")
print("=====================================================================")

class university:
    uniName = ""
    uniCity = ""
    uniAge = ""

    def  universityInformation(self):
        print("--------------------------------------------------------------------")
        print("Name of the University is " + self.uniName)
        print("It is located in " + self.uniCity )
        print("University age = " + str(self.uniAge) + " years")
        print("--------------------------------------------------------------------")

class teacher:
    tchName = ""
    tchAge = ""
    tchSal = ""

    def  teacherInformation(self):
        print("--------------------------------------------------------------------")
        print("Name of the teacher is " + self.tchName)
        print("The age of teacher is " + str(self.tchAge) + " years")
        print("The salary of teacher is " + str(self.tchSal) + " Riyal")
        print("--------------------------------------------------------------------")

uni = university()
uni.uniName = "Superior"
uni.uniCity = "Lahore"
uni.uniAge = 40
uni.universityInformation()

tch = teacher()
tch.tchName = "Waqas"
tch.tchAge = 25
tch.tchSal = 10000
tch.teacherInformation()
print("All is good")


## Task 02
# Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.

print("=====================================================================")
print("                                Task 02                              ")
print("=====================================================================")