# ___________________________________________Project One
from functools import reduce
# 1
class Person:
    def __init__(self , Name , Address ):
        self._Name = Name
        self._Address = Address

    def getName(self):
        return self._Name

    def setName(self , Name):
        self._Name = Name

    def getAddress(self):
        return self._Address

    def setAddress(self , Address):
        self._Address = Address

    def __del__(self):
        print(' I have been deleted')


person=Person("Raghad","Amman")
print(person.getName())
print(person.getAddress())

del person
# 2

class Employee(Person):
    def __init__(self , Number , Salary , JopTitle ,  Name , Address):
        super().__init__(Name , Address)
        self.Number = Number
        self.__Salary = Salary
        self.__JopTitle = JopTitle
        self.__Loans = []


    def getNumber(self):
        return self.Number
    def getSalary(self):
        return self.__Salary

    def setSalary(self , Salary):
        self.__Salary = Salary

    def getJopTitle(self):
        return  self.__JopTitle

    def setJopTitle(self , JopTitle):
        self.__JopTitle = JopTitle

    def getTotalLoans(self):
        total = 0
        for elem in range (len(self.__Loans)):
            total += self.__Loans[[elem]]
        return total

    def getMaxLon(self):
        if len(self.__Loans) != 0 :
            return (max(self.__Loans))
        else :
            return 0

    def getMinLon(self):
        if len(self.__Loans) != 0:
            return (min(self.__Loans))

    def setLons(self,Lons):
        self.__Loans = Lons


    def printInfo(self):
        return self.getName(), self.getAddress(), self.getJopTitle(), self.getSalary()


    def __del__(self):
        newDic = reduce (lambda x, y: x if x > y else y, dic, 0)
        return newDic



emp = Employee(1, 500 ,'full stack','Mohammed',"Consultant")
emp.printInfo()
# 3

class Student:
    def __init__(self , Number, Name , Subject ,Marks):
        self.Number = Number
        self.__Name = Name
        self.__Subject = Subject
        self.__Marks = Marks

    def getSubject(self , Subject):
        return self.__Subject