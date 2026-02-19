#budget tool

import budget
import blogs 

#import summary

Transactions = {}
rules = """
	1. Exit
	2. Enter Budget
	3. Input a transaction

"""
while True:
	print(rules)
	n = int(input("\n Enter Number: "))
	if n == 2:
		budget.get_budget()
	elif n == 1:
		print("Thank you for using the budget tool")
		break
	elif n == 3: 
		blogs.create_Transactions(Transactions)


