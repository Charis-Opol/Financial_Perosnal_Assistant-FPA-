"""import budget
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
        print(f"{item['name']}: ${item['amount']}")"""


import budget
import blogs

class BudgetTracker:
    def __init__(self, budget_service: budget.BudgetService, transaction_manager: blogs.TransactionManager):
        self.budget_service = budget_service
        self.transaction_manager = transaction_manager
        self.current_budget = None

    def setup(self):
        self.current_budget = self.budget_service.get_budget()

    def add_transaction(self):
        self.transaction_manager.add()

    def cumulative_expense(self):
        return sum(t.amount for t in self.transaction_manager.transactions)

    def remaining(self):
        return self.current_budget - self.cumulative_expense()

    def is_over_budget(self):
        return self.cumulative_expense() > self.current_budget


class ConsoleBudgetDisplay:
    def show_summary(self, tracker: BudgetTracker):
        print("\n--- Financial Summary ---")
        print(f"Cumulative expense: UGX{tracker.cumulative_expense()}")
        print(f"Remaining: UGX{tracker.remaining()}")

    def show_status(self, tracker: BudgetTracker):
        if tracker.is_over_budget():
            print("⚠️  Alert: You have exceeded your budget!")
        else:
            print("✅ Success: You are within your budget.")


# --- Wiring it all up ---
input_handler = budget.BudgetInput()
validator = budget.BudgetValidator()
budget_service = budget.BudgetService(input_handler, validator)

transaction_manager = blogs.TransactionManager()

tracker = BudgetTracker(budget_service, transaction_manager)
display = ConsoleBudgetDisplay()

tracker.setup()
tracker.add_transaction()

display.show_summary(tracker)
display.show_status(tracker)