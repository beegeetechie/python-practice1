expense = (int(input("enter the number of expenses\n")))
expenses = []
total = 0
for i in range(expense):
  expenses.append(float(input("enter expense :")))
total = sum(expenses)
#print('Total Expense is $',total, sep='')
print("Total Expenses is $" + str(total))