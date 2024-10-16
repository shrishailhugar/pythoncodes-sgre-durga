class Employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday
    def __mul__(self,other):
        return self.salaryperday*other.no_of_working_days
class timesheet:
    def __init__(self,name,no_of_working_days):
        self.name=name
        self.no_of_working_days=no_of_working_days
    def __mul__(self,other):
        return self.no_of_working_days*other.salaryperday

e1=Employee('e1',2000)
t1=timesheet('e1',20)
print('salary of this month',t1*e1)
print('salary of this month',e1*t1)
