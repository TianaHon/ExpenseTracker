# ExpenseTrackerCollabProject

import os
import time
import datetime

# Import the ‘os’ module and clear the screen
def clear_screen():
    time.sleep(2) # wait 2s to clear screen
    os.system('cls' if os.name == 'nt' else 'clear') # for Windows and iOS

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        return None

 # Store a expense (category, amount, etc.)   
def save_expense(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']},{expense('date')}\n")   

# input and store a expense (category, amount, date)
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = []
            for line in file:
                category, amount, date = line.strip().split(',')
                expenses.append({"category": category, "amount": amount, "date": date})
            return expenses
    except FileNotFoundError:
        return [] 
 
# Expenses should have catepory , amount and date   
def add_expense(expenses):
    category = input("Enter the category: ")
    amount = input("Enter the amount: ")
    date_str = input("Enter the date (dd/mm/yyyy): ")
    date = validate_date(date_str)
    if not date:
        print("Wrong date format. Please use dd/mm/yyyy.")
        return
    expenses.append({"category": category, "amount": amount, "date": date_str})
    print("Expenses added.")

# View all expenses
def view_expense(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("\nYour expenses:")
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

# Filter expenses by category
def filter_expense(expenses):
    filter = input("Filter by (week/month/year): ").lower()
    filtered = {}

    for expense in expenses:
        date_obj = datetime.datetime.strptime(expense['date'], "%d/%m/%Y")
        key = None

        if filter == "week":
            key = date_obj.strftime("%Y-W%U")
        elif filter == "month":
            key = date_obj.strftime("%Y-%m")
        elif filter == "year":
            key = date_obj.strftime("%Y")
        else:
            print("Invalid period.")



# Calculate the total expenses
def calculate_reminder(expenses):
    
# Delete specific expenses
def delete_expense(expenses):
    view_expense(expenses):
    category = input("Enter the category of the expense to delete: ")
    date = input("Enter the date (dd/mm/yyyy) of the expense to delete: ")

# Main reminder
def main():
    expenses = load_expenses()  # Load existing reminders from file
    while True:
        clear_screen()
        print("---- Expense Tracker ----")
        print("1. Add a new expenses")
        print("2. View all expenses")
        print("3. Filter expenses by category")
        print("4. Calculate the total expenses")
        print("5. Delete specific expenses")
        print("6. Save and Exit")
        print("7. Exit without saving")
        
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expense(expenses)
        elif choice == "3":
            filter_expense(expenses)
        elif choice == "4":
            calculate_reminder(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            save_expense(expenses)
            print("Expense saved. Exiting...")
            break
        elif choice == "7":
            print("Exiting without saving.")
            break
        else:
            print("Wrong choice. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()