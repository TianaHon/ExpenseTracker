import os
import time
import datetime

# Import the ‘os’ module and clear the screen
def clear_screen():
    time.sleep(2)  # Wait 2s to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')  # For Windows and Linux/macOS


# Validate date format
def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%d/%m/%Y") # convert string to datetime
    except ValueError:
        return None # return None if format is invalid


# Store expenses (category, amount, date)
def save_expenses(expenses):
    with open("expenses.txt", "w") as file: # open file in write mode
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']},{expense['date']}\n") # write each expense to file in correct format


# Load expenses from file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file: # open file in read mode
            expenses = []
            for line in file:
                category, amount, date = line.strip().split(',') # split line into category, amount, and date
                expenses.append({"category": category, "amount": amount, "date": date}) # add expense to list
            return expenses
    except FileNotFoundError:
        return [] # return empty list if file not found


# Input and store an expense (category, amount, date)
def add_expense(expenses):
    category = input("Enter the category: ") # input for category
    amount = input("Enter the amount: ") # input for amount

    # Ensure amount is a valid number
    try:
        amount = float(amount) # convert amount to float
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return # if amount is not a valid number, return to main menu

    date_str = input("Enter the date (dd/mm/yyyy): ") # input for date
    date = validate_date(date_str) # validate date format
    if not date:
        print("Wrong date format. Please use dd/mm/yyyy.")
        return # if date is not in correct format, return to main menu

    expenses.append({"category": category, "amount": amount, "date": date_str}) # add expense to list
    save_expenses(expenses)  # Save after adding a new expense
    print("Expense added successfully.")


def calculate_total_expenses(expenses):
    total = 0 # initialize total to 0
    for expense in expenses:
        total += float(expense["amount"]) # add amount to total
    return total


# View expenses (category, amount, date) 
def view_expenses(total):
    if expenses == []:
        print("No expenses recorded.")
        return
    print("\nExpense List:")
    expenses.sort(key=lambda x: x["category"])  # Sort by category for grouping
    current_category = None # initialize current category to None
    for expense in expenses:
        if expense["category"] != current_category: # if category is different from current category
            current_category = expense["category"] # update current category
            print(f"\nCategory: {current_category.capitalize()}") # print category name with first letter capitalized
        print(f"Date: {expense['date']}, Amount: {expense['amount']}")
    

# deletes expenses from list
def delete_expense(expenses):
    category = input("Enter the category of the expense to delete: ") # input for category to delete from
    
    date = input("Enter the date of the expense to delete (dd/mm/yyyy): ") # input for date to delete from
    # Validate date format
    date = validate_date(date)
    if not date:
        print("Wrong date format. Please use dd/mm/yyyy.")
        return
        
    amount = input("Enter the amount of the expense to delete: ") # input for amount to delete
    # Ensure amount is a valid number
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
        
    for expense in expenses:
        if expense["category"] == category and expense["date"] == date and float(expense["amount"]) == amount: # if category, date, and amount match
            expenses.remove(expense) # removes matched expense from list
            save_expenses(expenses)  # Save after deleting an expense
            print("Expense deleted successfully.")
            return
        else:
            print("Expense not found.")
            return


def main():
    action = input("\nExpense Tracker Menu:\na. Add expense\nb. View expenses\nc. Show total expense\nd. Delete expense from list\ne. Exit\nEnter your choice: ")
    if action == "a":
        expenses = load_expenses()
        add_expense(expenses)
        clear_screen()
    if action =="b":
        expenses = load_expenses()
        print("Expense List:")
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
        print("\nScreen will clear in 5 seconds.")
        time.sleep(5)
        clear_screen()
    if action == "c":
        expenses = load_expenses()  # Load expenses before calculation
        total = calculate_total_expenses(expenses)
        print("Total expenses: ${:.2f}".format(total))
        clear_screen()
    if action == "d":
        expenses = load_expenses()
        delete_expense(expenses)
        clear_screen()
    if action == "e":
        print("Exiting the program.")
        clear_screen()
    else:
        print("Invalid choice. Please try again.")
        clear_screen()
        
while True:
    main()