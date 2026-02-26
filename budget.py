
'''def get_budget():
    while True:
        budget_start = int (input("Enter your budget amount for the week >> "))

        if budget_start < 0: 
            print("Budget can't be negative. Please enter again.")
        else:
            return budget_start
        '''




class BudgetInput:
    def get_input(self) -> int:
        return int(input("Enter your budget amount for the week >> "))


class BudgetValidator:
    def is_valid(self, amount: int) -> bool:
        return amount > 0


class BudgetService:
    def __init__(self, input_handler: BudgetInput, validator: BudgetValidator):
        self.input_handler = input_handler
        self.validator = validator

    def get_budget(self) -> int:
        while True:
            amount = self.input_handler.get_input()

            if not self.validator.is_valid(amount):
                print("Budget can't be negative. Please enter again.")
            else:
                return amount


# Usage
input_handler = BudgetInput()
validator = BudgetValidator()
budget_service = BudgetService(input_handler, validator)

budget = budget_service.get_budget()