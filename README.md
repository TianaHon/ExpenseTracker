# ExpenseTrackerCollabProject
import os
import time
import datetime

# Import the ‘os’ module and clear the screen
def clear_screen():
     time.sleep(1) # wait 1s to clear screen
     os.system('cls' if os.name == 'nt' else 'clear') # for Windows and iOS
     time.sleep(1)  # Wait 1s to clear the screen
     os.system('cls' if os.name == 'nt' else 'clear')  # For Windows and Linux/macOS

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        return None

 # Store a expense (category, amount, etc.)   
def save_expenses(expenses):
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
def add_expenses(expenses):
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
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("\nYour expenses:")
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

# Filter expenses by category
def filter_expenses(expenses):
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
            return  # Exit if invalid input
    
        filtered[key] = filtered.get(key, 0) + float(expense['amount'])  # Convert to float before adding
        
    for key, amount in filtered.items():
        print(f"{key}: ${amount:.2f}")

# Calculate the total expenses
def calculate_total_expenses(expenses):
    total = 0 # initialize total to 0
    for expense in expenses:
        total += float(expense["amount"]) # add amount to total
        print("Total expenses: ${:.2f}".format(total)) # print total expense with 2 decimal places
    return total

# deletes expenses from list
def delete_expense(expenses):
    category = input("Enter the category of the expense to delete: ") # input for category to delete from
    
    date = input("Enter the date of the expense to delete (dd/mm/yyyy): ") # input for date to delete from
    # Validate date format
    date = validate_date(date)
    if not date:
        print("Wrong date format. Please use dd/mm/yyyy.")
        return
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expenses added.")
        
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
        
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            filter_expenses(expenses)
        elif choice == "4":
            calculate_total_expenses(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            save_expenses(expenses)
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
        









    

