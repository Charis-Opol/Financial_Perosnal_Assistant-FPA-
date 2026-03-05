def report(initial_budget, transactions):
    """
    Generates a formatted financial summary of a budget session.
    
    Args:
        initial_budget (float): The starting amount of money.
        transactions (list): A list of dicts with 'name' (str) and 'amount' (float).
    """
    # Calculate total expenses safely
    total_expenses = sum(item.get('amount', 0) for item in transactions)
    final_position = initial_budget - total_expenses
    
    # --- Header ---
    print("\n" + "="*40)
    print("        FINAL FINANCIAL REPORT")
    print("="*40)
    print(f"Initial Budget:          ${initial_budget:,.2f}")
    print(f"Total Recorded Expenses: ${total_expenses:,.2f}")
    print("-" * 40)
    
    # --- Determine Surplus or Deficit ---
    if final_position >= 0:
        print(f"Remaining Balance:       ${final_position:,.2f} (Surplus)")
    else:
        # Use abs() to avoid a "double negative" sign
        print(f"Financial Deficit:      -${abs(final_position):,.2f} (Overspent)")
    
    # --- Itemized Log ---
    print("\n--- ITEMIZED TRANSACTION LOG ---")
    if not transactions:
        print("No transactions were recorded during this session.")
    else:
        for i, item in enumerate(transactions, 1):
            name = item.get('name', 'Unknown')
            amount = item.get('amount', 0.0)
            print(f"{i}. {name:<20} | ${amount:>10,.2f}")
    
    # --- Footer ---
    print("="*40)
    print("        End of Session Report")
    print("="*40 + "\n")

# --- Example Usage (Main block) ---
if __name__ == "__main__":
    # 1. Define your starting budget
    my_budget = 1500.00
    
    # 2. Define your list of transactions
    my_transactions = [
        {"name": "Groceries", "amount": 150.50},
        {"name": "Internet Bill", "amount": 60.00},
        {"name": "New Mechanical Keyboard", "amount": 125.00},
        {"name": "Coffee Shop", "amount": 12.75}
    ]
    
    # 3. Call the function
    report(my_budget, my_transactions)