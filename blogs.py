def create _Transactions():
    Transactions = {}
    Transactions_name = input("What do you want to spend on today? ")
    amount = int(input("How much do you want to spend on "))
    Transactions[Transactions_name] = amount

    return Transactions
