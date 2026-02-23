def report(initial_budget, transactions):
    # Calculate total expenses
    total_expenses = sum(item['amount'] for item in transactions)
    final_position = initial_budget - total_expenses
    
    print("\n" + "="*40)
    print("        FINAL FINANCIAL REPORT")
    print("="*40)
    print(f"Initial Budget:          ${initial_budget:,.2f}")
    print(f"Total Recorded Expenses: ${total_expenses:,.2f}")
    print("-" * 40)
    
    # Determine Surplus or Deficit
    if final_position >= 0:
        print(f"Remaining Balance:       ${final_position:,.2f} (Surplus)")
    else:
        print(f"Financial Deficit:      -${abs(final_position):,.2f} (Overspent)")
    
    print("\n--- ITEMIZED TRANSACTION LOG ---")
    if not transactions:
        print("No transactions were recorded during this session.")
    else:
        for i, item in enumerate(transactions, 1):
            print(f"{i}. {item['name']:<20} | ${item['amount']:>10,.2f}")
    
    print("="*40)
    print("        End of Session Report")
    print("="*40 + "\n")