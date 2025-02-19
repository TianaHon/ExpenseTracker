import os
import time
import datetime

# Function to clear the screen
def clear_screen():
    time.sleep(1)  # Wait 1 second before clearing
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for Windows & Linux/macOS

# Function to validate date format
def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%d/%m/%Y")  # Convert string to datetime
    except ValueError:
        return None  # Return None if the format is invalid

# Function to save expenses to a file
def save_expenses(expenses):
    with open("expenses.txt", "w") as file:  # Open file in write mode
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']},{expense['date']}\n")  # Save in correct format

# Function to load expenses from file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:  # Open file in read mode
            return [{"category": c, "amount": float(a), "date": d} for c, a, d in (line.strip().split(',') for line in file)]
    except FileNotFoundError:
        return []  # Return empty list if the file does not exist

# Function to add a new expense
def add_expense(expenses):
    category = input("Enter category: ").strip().lower()

    try:
        amount = float(input("Enter amount: ").strip())  # Convert amount to float
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    date_str = input("Enter date (dd/mm/yyyy): ").strip()
    if not validate_date(date_str):  # Validate date format
        print("Wrong date format. Use dd/mm/yyyy.")
        return

    expenses.append({"category": category, "amount": amount, "date": date_str})  # Add expense
    save_expenses(expenses)  # Save after adding
    print(f"Expense added under '{category}'.")

# Function to view expenses, grouped by category
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    expenses.sort(key=lambda x: x["category"])  # Sort by category for grouping
    current_category = None

    print("\nExpense List (Grouped by Category):")
    for expense in expenses:
        if expense["category"] != current_category:  # Print category header only when it changes
            current_category = expense["category"]
            print(f"\nCategory: {current_category.capitalize()}")

        print(f"  - Date: {expense['date']}, Amount: ${expense['amount']:.2f}")

# Function to filter expenses by time period (week/month/year)
def filter_expenses(expenses):
    filter_type = input("Filter by (week/month/year): ").strip().lower()
    filtered = {}

    for expense in expenses:
        date_obj = validate_date(expense['date'])
        if not date_obj:
            continue  # Skip invalid dates

        if filter_type == "week":
            key = date_obj.strftime("%Y-W%U")  # Year-Week format
        elif filter_type == "month":
            key = date_obj.strftime("%Y-%m")  # Year-Month format
        elif filter_type == "year":
            key = date_obj.strftime("%Y")  # Year format
        else:
            print("Invalid period.")
            return

        filtered[key] = filtered.get(key, 0) + expense['amount']  # Sum expenses for the selected period

    for key, amount in filtered.items():
        print(f"{key}: ${amount:.2f}")

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)  # Calculate total sum
    print(f"Total expenses: ${total:.2f}")

# Function to delete an expense
def delete_expense(expenses):
    category = input("Enter category to delete: ").strip().lower()
    date_str = input("Enter date (dd/mm/yyyy): ").strip()
    if not validate_date(date_str):
        print("Wrong date format. Use dd/mm/yyyy.")
        return

    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    for expense in expenses:
        if expense["category"] == category and expense["amount"] == amount and expense["date"] == date_str:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully.")
            return

    print("Expense not found.")  # Only print if no match was found

# Main function
def main():
    expenses = load_expenses()  # Load expenses once at the start
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add expense")
        print("2. View expenses (Grouped)")
        print("3. Filter expenses by time period")
        print("4. Show total expenses")
        print("5. Delete expense")
        print("6. Save and Exit")
        print("7. Exit without saving")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_expense(expenses)
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
            print("Expenses saved. Exiting...")
            break
        elif choice == "7":
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")  # Prevents instant screen clearing
        clear_screen()

# Run the program
if __name__ == "__main__":
    main()
