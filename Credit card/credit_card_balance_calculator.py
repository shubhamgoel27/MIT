balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

def balance_calculator(balance, annualInterestRate, monthlyPaymentRate):
	monthlyPayment = monthlyPaymentRate * balance
	balance = balance - monthlyPayment
	
	balance = balance + (annualInterestRate/12)*balance
	return balance,monthlyPayment

for month in range(1,13):
	balance, monthlyPayment = balance_calculator(balance, annualInterestRate, monthlyPaymentRate)
	print "Month:" +  str(month)
	print "Minimum monthly payment: " +  str(round(monthlyPayment,2))
	print "Remaining balance: " +  str(round(balance,2))
	totalPaid += monthlyPayment

print "Total paid: " + str(round(totalPaid,2))
print "Remaining balance: " + str(round(balance,2))

print "Bhai git seekh liya to aur kya chahiye"