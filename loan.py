#Loan calculator
money_owed = float(input("Enter the amount owed:"))#50000
roi = float(input("Enter the Rate of Interest:")) #3
emi = float(input("Enter the monthly EMI:")) #1000
months = int(input("How many months you would like to see the results:"))

for i in range(months):
  monthly_rate = money_owed * roi/100/12
  money_owed = money_owed + monthly_rate

  if(money_owed - emi < 0):
      print("Last EMI is", money_owed)
      print("You paid off the loan in", i+1, 'months')
      break;
  money_owed = money_owed - emi
  print("Paid is",emi*(i+1),",oustanding is",money_owed,",of which interest is",monthly_rate)