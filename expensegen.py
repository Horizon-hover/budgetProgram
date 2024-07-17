def get_expense_input(expense_name, period):
    while True:
        try:
            if period == 'weekly':
                expense = float(input(f"Enter your weekly {expense_name} expense (£): "))
                return expense * 4  # Convert weekly expense to monthly
            else:
                return float(input(f"Enter your monthly {expense_name} expense (£): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_income_input(period):
    while True:
        try:
            if period == 'weekly':
                income = float(input("Enter your weekly income (£): "))
                return income * 4  # Convert weekly income to monthly
            else:
                return float(input("Enter your monthly income (£): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_total_expenses(expenses):
    return sum(expenses.values())

def display_monthly_report(income, expenses):
    print("\nMonthly Budget Summary")
    print("----------------------")
    print(f"Income: £{income:.2f}")
    for expense_name, amount in expenses.items():
        print(f"{expense_name.capitalize()}: £{amount:.2f}")
    total_expenses = calculate_total_expenses(expenses)
    print("----------------------")
    print(f"Total Monthly Expenses: £{total_expenses:.2f}")
    predict_spending(income, total_expenses)

def display_weekly_report(income, expenses):
    print("\nWeekly Budget Summary")
    print("----------------------")
    weekly_income = income / 4
    print(f"Weekly Income: £{weekly_income:.2f}")
    for expense_name, amount in expenses.items():
        weekly_expense = amount / 4
        print(f"Weekly {expense_name.capitalize()}: £{weekly_expense:.2f}")
    total_weekly_expenses = calculate_total_expenses(expenses) / 4
    print("----------------------")
    print(f"Total Weekly Expenses: £{total_weekly_expenses:.2f}")
    predict_spending(weekly_income * 4, total_weekly_expenses * 4)

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
        while True:
            period = input("Would you like to input your expenses in monthly, weekly terms, or exit? (monthly/weekly/exit): ").strip().lower()
            if period in ['monthly', 'weekly', 'exit']:
                break
            else:
                print("Invalid choice. Please select 'monthly', 'weekly', or 'exit'.")

        if period == 'exit':
            print("Exiting the program.")
            break
        
        # Collect income data
        income = get_income_input(period)
        
        # Collect expense data
        expenses = {}
        expenses['groceries'] = get_expense_input("groceries", period)
        expenses['electric'] = get_expense_input("electric", period)
        expenses['gas'] = get_expense_input("gas", period)
        
        while True:
            additional_expense_name = input("Enter an additional expense name (or 'done' to finish): ").strip()
            if additional_expense_name.lower() == 'done':
                break
            expenses[additional_expense_name] = get_expense_input(additional_expense_name, period)
        
        # Display the monthly report
        display_monthly_report(income, expenses)
        
        # Ask the user for the next step
        while True:
            next_step = input("Would you like to see the weekly breakdown report, input new amounts, or exit? (weekly/new/exit): ").strip().lower()
            if next_step == 'weekly':
                display_weekly_report(income, expenses)
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









