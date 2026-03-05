import budget
import blogs

class BudgetTracker:
    def __init__(self, budget_service: budget.BudgetService, transaction_manager: blogs.TransactionManager):
        self._budget_service = budget_service          
        self._transaction_manager = transaction_manager  
        self._current_budget = None                    

    def setup(self):
        self._current_budget = self._budget_service.get_budget()

    def add_transaction(self):
        self._transaction_manager.add()

    @property
    def cumulative_expense(self) -> float:             # getter
        return sum(t.amount for t in self._transaction_manager.transactions)

    @property
    def remaining(self) -> float:                      # immutable
        return self._current_budget - self.cumulative_expense

    @property
    def is_over_budget(self) -> bool:
        return self.cumulative_expense > self._current_budget

    @property
    def current_budget(self) -> float:                 
        return self._current_budget


class ConsoleBudgetDisplay:
    def show_summary(self, tracker: BudgetTracker):
        print("\n--- Financial Summary ---")
        print(f"Cumulative expense: UGX{tracker.cumulative_expense}") 
        print(f"Remaining: UGX{tracker.remaining}")                    

    def show_status(self, tracker: BudgetTracker):
        if tracker.is_over_budget:                                     
            print("⚠️  Alert: You have exceeded your budget!")
        else:
            print("✅ Success: You are within your budget.")