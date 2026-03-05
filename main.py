# main.py

from budget         import BudgetValidator, BudgetService, BudgetInput
from blogs          import TransactionManager
from fiscaloversite import BudgetTracker, ConsoleBudgetDisplay
from summary        import Transaction, ReportCalculator, ReportFormatter, ConsoleReportPrinter, FinancialReport

MENU = """
    1. Exit
    2. Enter Budget
    3. Input a transaction

    Review (Fiscal Oversite)

    4. Display Expenses
    5. Check Budget Status
    6. Budget Summary
"""


class App:
    """Composes all services and runs the menu loop."""

    def __init__(self):
        self._tracker   = BudgetTracker(BudgetService(BudgetInput(), BudgetValidator()), TransactionManager())
        self._display   = ConsoleBudgetDisplay()
        self._formatter = ReportFormatter()
        self._printer   = ConsoleReportPrinter()

    def run(self) -> None:
        while True:
            print(MENU)
            try:
                n = int(input(" Enter Number: "))
            except ValueError:
                print("Please enter a valid number from the menu.")
                continue

            if   n == 1: self._exit(); break
            elif n == 2: self._set_budget()
            elif n == 3: self._add_transaction()
            elif n == 4: self._display_expenses()
            elif n == 5: self._check_status()
            elif n == 6: self._show_summary()
            else:        print("Invalid choice. Please select 1-6.")

    # ── private actions ───────────────────────────────────────────────────────

    def _exit(self):
        print("Thank you for using the budget tool. Goodbye!")

    def _set_budget(self):
        self._tracker.setup()
        print(f"Budget set to: UGX{self._tracker.current_budget:,.2f}")

    def _add_transaction(self):
        self._tracker.add_transaction()

    def _display_expenses(self):
        print(f"\nCumulative Expenses: UGX{self._tracker.cumulative_expense:,.2f}")

    def _check_status(self):
        self._display.show_status(self._tracker)

    def _show_summary(self):
        transactions = [
            Transaction(transactions.name, transactions.amount)
            for transactions in self._tracker._transaction_manager.transactions
        ]
        FinancialReport(
            ReportCalculator(self._tracker.current_budget, transactions),
            self._formatter,
            self._printer,
        ).generate()


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    App().run()