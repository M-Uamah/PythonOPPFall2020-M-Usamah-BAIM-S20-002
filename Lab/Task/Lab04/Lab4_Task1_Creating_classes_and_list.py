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
        print("Name of the teacher is Sir " + self.tchName)
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


## Task 02
# Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.

print("=====================================================================")
print("                                Task 02                              ")
print("=====================================================================")

# creating 5 object for university
uni1 = university()
uni1.uniName = "Superior"
uni1.uniCity = "Lahore"
uni1.uniAge = 40

uni2 = university()
uni2.uniName = "University of Central Punjab"
uni2.uniCity = "Lahore"
uni2.uniAge = 20

uni3 = university()
uni3.uniName = "University of Lahore"
uni3.uniCity = "Lahore"
uni3.uniAge = 60

uni4 = university()
uni4.uniName = "Agriculture University"
uni4.uniCity = "Faisalabad"
uni4.uniAge = 90

uni5 = university()
uni5.uniName = "King Fahad University"
uni5.uniCity = "Dammam"
uni5.uniAge = 110

#list of university
uniList = [uni1, uni2, uni3, uni4, uni5]

# for loop
for eachUni in  uniList:
    eachUni.universityInformation()

# creating 5 object for teacher

tch1 = teacher()
tch1.tchName = "Waqas"
tch1.tchAge = 25
tch1.tchSal = 10000

tch2 = teacher()
tch2.tchName = "Omer"
tch2.tchAge = 52
tch2.tchSal = 15000

tch3 = teacher()
tch3.tchName = "Ahmed"
tch3.tchAge = 28
tch3.tchSal = 11000

tch4 = teacher()
tch4.tchName = "Bilai"
tch4.tchAge = 31
tch4.tchSal = 13000

tch5 = teacher()
tch5.tchName = "Ali"
tch5.tchAge = 29
tch5.tchSal = 9000

#List of teachers
tchList = [tch1, tch2, tch3, tch4, tch5]

#by for loop
for eachTch in tchList:
    eachTch.teacherInformation()
