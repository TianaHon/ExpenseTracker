import os
import time
import datetime

# Import the ‘os’ module and clear the screen
def clear_screen():
    time.sleep(2)
    os.system('cls') #Windows

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

