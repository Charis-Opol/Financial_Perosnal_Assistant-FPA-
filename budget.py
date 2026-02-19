
def get_budget():
    while True:
        budget_start = int (input("Enter your budget amount for the week >> "))

        if budget_start < 0: 
            print("Budget can't be negative. Please enter again.")
        else:
            return budget_start
        




