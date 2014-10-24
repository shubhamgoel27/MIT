balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0

def end_of_year_balance(balance, monthlyInterestRate, monthlyPayment):
	for i in range(12):
		balance = balance - monthlyPayment
		balance = balance + monthlyInterestRate*balance
	return balance	

for monthlyPayment in range(0,450,10):
	temp_balance = end_of_year_balance(balance,monthlyInterestRate,monthlyPayment)
	if temp_balance <=0:
		print "Lowest Payment: " + str(monthlyPayment)
		break

