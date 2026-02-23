import budget
import blogs


def calculate_cumulative(transaction_list):
    total = 0
    # Assuming transaction_list is a list of dictionaries: [{'name': 'item', 'amount': 10}, ...]
    for item in transaction_list:
        total += item['amount']
    return total

def display_expense(current_budget, transaction_list):
    cum_expense = calculate_cumulative(transaction_list)
    remaining = current_budget - cum_expense
    
    print(f"\n--- Financial Summary ---")
    print(f"Your cumulative expense is: UGX{cum_expense}")
    print(f"You are remaining with: UGX{remaining}")

def check_budget(current_budget, transaction_list):
    cum_expense = calculate_cumulative(transaction_list)
    
    if cum_expense > current_budget:
        print("\n⚠️ Alert: You have exceeded your budget!")
    else:
        print("\n Success: You are within your budget.")

def index_transactions(transaction_list):
    print("\n--- Transaction History ---")
    for item in transaction_list:
        print(f"{item['name']}: ${item['amount']}")