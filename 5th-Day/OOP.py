# Exercise 1 ___________________________________________________
# Write a python program to create an Employee Class


class Employee :
    def __init__(self , Number , Name , Address , Salary , JopTitle):
        self.Number = Number
        self.__Name = Name
        self.__Address = Address
        self.__Salary = Salary
        self.__JopTitle = JopTitle

    def  getName (self):
        return self.__Name

    def getAddress(self):
        return self.__Address

    def getSalary(self):
        return self.__Salary

    def getJopTitle(self):
        return self.__JopTitle

    def setAddress(self , Address):
        self.__Address = Address
        print(self.__Address)


    def __del__(self):
        print(self.__Name +' Has been Deleted' )


employee = Employee(133 ,"Raghad", "Amman ", 1000 , " Full Stack")
print( employee.getName())
print( employee.getJopTitle())
print( employee.getSalary())
employee.setAddress('Jordan')
employee.__del__()

print()


# Exercise 2 ____________________________________________________
# Create the following object form type Employee

EmployeeOne = Employee(1, "Mohammad Khalid" , "Amman,Jordan", 500 ,"Consultant")
EmployeeTwo = Employee(2, "Hala Rana" , "Aqaba,Jordan", 750 ,"Manager")




# Exercise 3 _____________________________________________________
# Build two print Function inside the class to print the following formats

class Employee :
    def __init__(self , Number , Name , Address , Salary , JopTitle):
        self.Number = Number
        self.__Name = Name
        self.__Address = Address
        self.__Salary = Salary
        self.__JopTitle = JopTitle

    def  getName (self):
        return self.__Name

    def getAddress(self):
        return self.__Address

    def getSalary(self):
        return self.__Salary

    def getJopTitle(self):
        return self.__JopTitle

    def setAddress(self , Address):
        self.__Address = Address
        print(self.__Address)


    def __del__(self):
        print(self.__Name +' Has been Deleted' )


    def printFomatOne(self):
        print('Employee One Information :')
        print('Employee Number :' , self.Number)
        print('Name :',self.__Name)
        print('Address :' , self.__Address)
        print('Salary :' , self.__Salary)
        print('Jop Title : ', self.__JopTitle)

        print()


    def printFrmatTwo(self):
        print('Employee Two Information : Employee Number = ', self.Number ,", Name = ", self.__Name ,', Address = ', self.__Address , ", Salary = ", self.__Salary , " , Jop Title \"" , self.__JopTitle , "\"")



EmployeeOne = Employee(1, "Mohammad Khalid" , "Amman,", 500 ,"Consultant")
EmployeeOne.printFrmatTwo()
EmployeeTwo = Employee(2, "Hala Rana" , "Aqaba,Jordan", 750 ,"Manager")
EmployeeTwo.printFrmatTwo()


# Exercise 4 _____________________________________________________
# Delete Both Object


del EmployeeOne

del EmployeeTwo
