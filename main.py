import budget
import blogs 
import fiscaloversite
import summary

rules = """
    1. Exit
    2. Enter Budget
    3. Input a transaction
    
    Review (Fiscal Oversite)
    
    4. Display Expenses
    5. Check Budget
    6. Budget Summary
"""

# Initialize your data at the start
my_budget = 0
my_transactions = [] 

while True:
    print(rules)
    
    # Capture the user choice
    try:
        n = int(input("\n Enter Number: "))
    except ValueError:
        print("Please enter a valid number from the menu.")
        continue
    
    if n == 1:
        print("Thank you for using the budget tool. Goodbye!")
        break
        
    elif n == 2:
        my_budget = budget.get_budget()
        print(f"Budget updated to: ${my_budget}")
        
    elif n == 3:
        blogs.create_Transactions(my_transactions)
        
    elif n == 4:
        fiscaloversite.display_expense(my_budget, my_transactions)
        
    elif n == 5:
        fiscaloversite.check_budget(my_budget, my_transactions)
        
    elif n == 6:
        summary.report(my_budget, my_transactions)
        
    else:
        print("Invalid choice. Please select 1-6.")