def create_Transactions(Transactions):
	name = input("What do you want to spend on today? ")
	amount = int(input("How much do you want to spend on "))
	Transactions['name'] = name
	Transactions['amount'] = amount
	
	return Transactions
