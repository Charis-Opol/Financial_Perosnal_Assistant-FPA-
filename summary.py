import blogs
import budget


total_expenses = 10
balance = total_expenses - budget.budget_start

print(f"""
	---------Financial Summmery---------
	Initial budget{budget.budget_start}\n
	\n
	Sum of expenseses = {total_expenses}\n
	Balance = {balance}\n\n

	Transations\n
	{blogs.transactions}

	

""")
