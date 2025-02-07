def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_expense_input(expense_name, period):
    prompt = f"Enter your {period} {expense_name} expense (£): "
    expense = get_numeric_input(prompt)
    return expense * 4 if period == 'weekly' else expense

def get_income_input(period):
    prompt = f"Enter your {period} income (£): "
    income = get_numeric_input(prompt)
    return income * 4 if period == 'weekly' else income

def display_report(income, expenses, period):
    print(f"\n{period.capitalize()} Budget Summary")
    print("----------------------")
    
    if period == 'weekly':
        income /= 4
        expenses = {k: v / 4 for k, v in expenses.items()}
    
    print(f"Income: £{income:.2f}")
    for expense_name, amount in expenses.items():
        print(f"{expense_name.capitalize()}: £{amount:.2f}")
    
    total_expenses = sum(expenses.values())
    print("----------------------")
    print(f"Total {period.capitalize()} Expenses: £{total_expenses:.2f}")
    predict_spending(income * (4 if period == 'weekly' else 1), total_expenses * (4 if period == 'weekly' else 1))

def predict_spending(total_income, total_expenses):
    remaining_budget = total_income - total_expenses
    if remaining_budget >= 0:
        print("\nYou are within your budget.")
    else:
        print("\nYou are over your budget.")
    
    print(f"Remaining budget for the month: £{remaining_budget:.2f}")
    weekly_budget = remaining_budget / 4
    print(f"Suggested weekly spending to stay within the budget: £{weekly_budget:.2f}")

def main():
    while True:
        print("Budget Generator")

        # Prompt user to input expenses in monthly, weekly terms, or exit
        period = input("Would you like to input your expenses in monthly, weekly terms, or exit? (monthly/weekly/exit): ").strip().lower()
        if period == 'exit':
            print("Exiting the program.")
            break
        elif period not in ['monthly', 'weekly']:
            print("Invalid choice. Please select 'monthly', 'weekly', or 'exit'.")
            continue
        
        # Collect income data
        income = get_income_input(period)
        
        # Collect expense data
        expenses = {}
        for expense_name in ['groceries', 'electric', 'gas']:
            expenses[expense_name] = get_expense_input(expense_name, period)
        
        while True:
            additional_expense_name = input("Enter an additional expense name (or 'done' to finish): ").strip()
            if additional_expense_name.lower() == 'done':
                break
            elif not additional_expense_name:
                print("Expense name cannot be empty.")
                continue
            expenses[additional_expense_name] = get_expense_input(additional_expense_name, period)
        
        # Display the report
        display_report(income, expenses, 'monthly')
        
        # Ask the user for the next step
        while True:
            next_step = input("Would you like to see the weekly breakdown report, input new amounts, or exit? (weekly/new/exit): ").strip().lower()
            if next_step == 'weekly':
                display_report(income, expenses, 'weekly')
                break
            elif next_step == 'new':
                break  # This will start the process over
            elif next_step == 'exit':
                print("Exiting the program.")
                return
            else:
                print("Invalid choice. Please select 'weekly', 'new', or 'exit'.")

if __name__ == "__main__":
    main()









