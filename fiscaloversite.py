import budget
import blogs

cum_expense = 0

budget_ = budget.budget_start()
transaction = blogs.transaction()

def index_transactions(transaction):
    for i in range(len(transaction)):
        print(f"{transaction.Transaction_name[i]}: {transaction.amount[i]}")


def cummulative_expense(transaction, cum_expense):
    for i in range(len(transaction)):
        cum_expense = cum_expense + transaction.amount[i]
    return cum_expense

def display_expense(cum_expense):
    print(f"Your cumulative expense is {cum_expense}")
    print(f"You are remaining with {budget_ - cum_expense} in your budget")

def check_budget(cum_expense, budget_):
    if cum_expense > budget_:
        print("You have exceeded your budget")
    else:
        print("You are within your budget")
