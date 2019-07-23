import datetime
class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def setBirthday(self,birthdate):
        self.birthdate = birthdate
    def getAge(self):
        return datetime.datetime.now().year - self.birthdate.year
    def risePay(self,percent):
        percent = float(percent.replace('%',''))/100
        self.salary = str(self.salary * (1 + percent))
        return self.salary

class PrivtTeacher(Teacher):
    nextIdNum = 1
    def __init__(self,name,salary):
        Teacher.__init__(self,name,salary)
        self.idNum = PrivtTeacher.nextIdNum
        PrivtTeacher.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    def getAge(self):
        return datetime.datetime.now().year - self.birthdate.year + 1

pt = PrivtTeacher('Mike',6000)
pt1 = Teacher('Mike',6000)
pt.setBirthday(datetime.date(1990,7,17))
pt1.setBirthday(datetime.date(1990,7,17))
print("重载的年龄：" + str(pt.getAge()))
print("未重载的年龄：" + str(pt1.getAge()))
