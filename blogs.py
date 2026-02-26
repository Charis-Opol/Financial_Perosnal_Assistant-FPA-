"""Transactions = {}

def create_Transactions(Transactions):
	name = input("What do you want to spend on today? ")
	amount = int(input("How much do you want to spend on "))
	Transactions['name'] = name
	Transactions['amount'] = amount
	
	return Transactions

def create_Transactions(transaction_list):
    name = input("What do you want to spend on today? ")
    amount = int(input(f"How much do you want to spend on {name}? "))
    
    new_entry = {
        'name': name,
        'amount': amount
    }
    
    transaction_list.append(new_entry)
    return transaction_list"""


class Transaction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add(self):
        name = input("What do you want to spend on? ")
        amount = int(input("Amount: "))
        self.transactions.append(Transaction(name, amount))

    def view(self):
        for t in self.transactions:
            print(f"{t.name} - ${t.amount}")

manager = TransactionManager()
manager.add()
manager.view()