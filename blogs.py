Transactions = {}

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
    return transaction_list