import csv
import os

FILE_NAME = "data.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Description"])

def add_transaction():
    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([t_type, amount, desc])

    print("✅ Transaction added!")

def view_transactions():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def show_balance():
    balance = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"] == "income":
                balance += float(row["Amount"])
            else:
                balance -= float(row["Amount"])

    print(f"💰 Current Balance: {balance}")

def menu():
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice")

menu()
