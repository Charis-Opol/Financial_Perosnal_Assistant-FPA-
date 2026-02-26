import unittest
from budget import BudgetValidator, BudgetService
from blogs import TransactionManager, Transaction
from main import BudgetTracker, ConsoleBudgetDisplay


# --- Fakes so we avoid real user input ---

class FakeBudgetInput:
    def get_input(self):
        return 500000


class FakeTransactionManager:
    def __init__(self, transactions):
        self.transactions = transactions

    def add(self):
        pass


# --- Tests ---

class TestBudgetTracker(unittest.TestCase):

    def setUp(self):
        budget_service = BudgetService(FakeBudgetInput(), BudgetValidator())
        self.transactions = [
            Transaction("Rent", 200000),
            Transaction("Groceries", 80000),
            Transaction("Transport", 30000),
        ]
        self.tracker = BudgetTracker(budget_service, FakeTransactionManager(self.transactions))
        self.tracker.setup()

    def test_cumulative_expense(self):
        self.assertEqual(self.tracker.cumulative_expense(), 310000)

    def test_remaining(self):
        self.assertEqual(self.tracker.remaining(), 190000)

    def test_within_budget(self):
        self.assertFalse(self.tracker.is_over_budget())

    def test_over_budget(self):
        budget_service = BudgetService(FakeBudgetInput(), BudgetValidator())
        tracker = BudgetTracker(budget_service, FakeTransactionManager([Transaction("Laptop", 600000)]))
        tracker.setup()
        self.assertTrue(tracker.is_over_budget())


if __name__ == '__main__':
    unittest.main()