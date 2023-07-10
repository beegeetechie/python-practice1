class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalariedEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    def paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, rate, hourly):
        super().__init__(fname,lname)
        self.rate = rate
        self.hourly = hourly
    def paycheck(self):
        return self.rate*self.hourly

class CommissionEmployee(SalariedEmployee):
    def __init__(self, fname, lname, salary, sales, commission):
        super().__init__(fname, lname, salary)
        self.sales = sales
        self.commission = commission
    def paycheck(self):
        normal_salary = super().paycheck()
        commission_salary = self.sales*self.commission
        return normal_salary + commission_salary
