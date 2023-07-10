#Company Class
from employee import Employee, SalariedEmployee, HourlyEmployee, CommissionEmployee

class Company:
  def __init__(self):
    self.employees=[]

  def add_employee(self,new_employee):
    self.employees.append(new_employee)
  def display_employee(self):
      for i in self.employees:
        print(i.fname, i.lname)
      print("________________")
  def display_pay(self):
    print("Paying Employees:")
    for i in self.employees:
      print("Paycheck for :",i.fname, i.lname)
      print(f'Amount: ${i.paycheck():,.2f}')
      print("________________")


def main():
  my_company = Company()
  employee1 = SalariedEmployee("Guru","Swami",50000)
  employee2 = HourlyEmployee("Ria","Bala",30,40)
  employee3 = CommissionEmployee("Ais","Bala",60000,5,100)
  my_company.add_employee(employee1)
  my_company.add_employee(employee2)
  my_company.add_employee(employee3)
  #my_company.display_employee()
  my_company.display_pay()

main()