# summary.py

class Transaction:
    def __init__(self, name: str, amount: float):
        self._name   = name
        self._amount = amount

    @property
    def name(self) -> str:
        return self._name

    @property
    def amount(self) -> float:
        return self._amount


class ReportCalculator:
    def __init__(self, initial_budget: float, transactions: list[Transaction]):
        self._initial_budget = initial_budget
        self._transactions   = transactions

    @property
    def initial_budget(self) -> float:
        return self._initial_budget

    @property
    def transactions(self) -> list[Transaction]:
        return list(self._transactions)

    @property
    def total_expenses(self) -> float:
        return sum(t.amount for t in self._transactions)

    @property
    def final_position(self) -> float:
        return self._initial_budget - self.total_expenses

    @property
    def is_surplus(self) -> bool:
        return self.final_position >= 0


class FinancialReport:
    """Composes calculator and prints the report directly."""

    WIDTH = 40

    def __init__(self, calculator: ReportCalculator):
        self._calc = calculator

    def generate(self) -> None:
        c = self._calc
        print("\n" + "=" * self.WIDTH)
        print("        FINAL FINANCIAL REPORT")
        print("=" * self.WIDTH)
        print(f"Initial Budget:          UGX {c.initial_budget:,.2f}")
        print(f"Total Recorded Expenses: UGX {c.total_expenses:,.2f}")
        print("-" * self.WIDTH)

        if c.is_surplus:
            print(f"Remaining Balance:       UGX {c.final_position:,.2f} (Surplus)")
        else:
            print(f"Financial Deficit:       UGX {abs(c.final_position):,.2f} (Overspent)")

        print("\n--- ITEMIZED TRANSACTION LOG ---")
        if not c.transactions:
            print("No transactions were recorded.")
        else:
            for i, t in enumerate(c.transactions, 1):
                print(f"{i}. {t.name:<20} | UGX {t.amount:>10,.2f}")

        print("=" * self.WIDTH)
        print("        End of Session Report")
        print("=" * self.WIDTH + "\n")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    transactions = [
        Transaction("Groceries",               150.50),
        Transaction("Internet Bill",            60.00),
        Transaction("New Mechanical Keyboard",  125.00),
        Transaction("Coffee Shop",               12.75),
    ]
    FinancialReport(ReportCalculator(1500.00, transactions)).generate()