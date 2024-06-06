import csv
import sys
import re
import os
import tabulate

def main():
    user = input("what is your name? ")
    print(f"Hello {user}, welcome to the Personal Finance Tracker")

    while True:
        print(f"How may I help you today? (press a number)\n1. Add an expense\n2. Calculate expense\n3. View expenses\n4. Exit the program")
        command = input("").strip()
        option = option_check(command)

        if option == 1:
            add_expense()
        elif option == 2:
            calculate_expense()
        elif option == 3:
            view_expense()
        elif option == 4:
            sys.exit("Exiting program. Goodbye👋")



def add_expense():
    expense_file = input("add a file: ").strip()

    if file_check(expense_file):

        while True:
            purchase, amount, date = input("provide your expense in a purchase, amount, and date format (i.e toy, $50.00, 2024-06-04)\n").strip().lower().split(',')
            if input_check(amount, date):
                break
            continue

        data = {"purchase":purchase.lower().strip(), "amount":amount.strip(), "date":date.strip()}
        append_dict(data, expense_file)
        print("Expense Added\n")
    else:
        print("provide a valid csv file\n")




def calculate_expense():
    calculate_file = input("add a file: ").strip()

    if file_check(calculate_file):
        with open(calculate_file, 'r') as file:
            reader = csv.DictReader(file)

            amount = 0
            for row in reader:
                try:
                    amount += float(row["amount"].replace('$','').strip())
                except ValueError:
                    print("unknown value in file provided\n")

            print(f"you have spent a total of ${amount}\n")
    else:
        print("provide a valid csv file\n")


def view_expense():
    view_file = input("add a file: ").strip()

    if file_check(view_file):
        with open(view_file, 'r') as file:
            expenses = []
            reader = csv.DictReader(file)
            for row in reader:
                 expenses.append(row)
        print(tabulate.tabulate(expenses, headers="keys", tablefmt="grid"))
        print()

    else:
        print("provide a valid csv file\n")




def option_check(command):
    while True:
        if command.isdigit() == False or not 0 < int(command) < 5:
            command = input("Choose from the corresponding list: ")
        else:
            return int(command)

def file_check(file):
    if file.endswith(".csv") and re.search(r"^(?:.+)\.csv$", file, re.IGNORECASE):
        return True
    return False

def input_check(amount, date):
    try:
        if not re.match(r"^\$?\d+(?:\.\d+)?$", amount.strip()):
            raise ValueError("Invalid amount format\n")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date.strip()):
            raise ValueError("Invalid date format\n")
        else:
            return True

    except ValueError as error:
        print(error)

def append_dict(dictionary, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as file:

        header = ["purchase", "amount", "date"]
        writer = csv.DictWriter(file, fieldnames=header)

        if not file_exists:
            writer.writeheader()

        writer.writerow(dictionary)



if __name__ == "__main__":
    main()
