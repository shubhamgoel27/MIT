balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
epsilon = 0.00005

lower = balance/12.0
upper = balance
for i in range(12):
	upper += monthlyInterestRate*upper

upper = upper/12.0

def end_of_year_balance(balance, monthlyInterestRate, monthlyPayment):
	for i in range(12):
		balance = balance - monthlyPayment
		balance = balance + monthlyInterestRate*balance
	return balance	

monthlyPayment = lower + upper
steps = 0 
while abs(end_of_year_balance(balance,monthlyInterestRate, monthlyPayment))>epsilon and steps<100:
	end_balance = end_of_year_balance(balance,monthlyInterestRate, monthlyPayment)
	#print "End balance: " + str(end_balance)
	if end_balance > 0:
		lower = monthlyPayment
	else:
		upper = monthlyPayment
	monthlyPayment = (lower + upper)/2.0
	#print monthlyPayment
	steps +=1

print "Lowest payment: " + str(round(monthlyPayment,2))