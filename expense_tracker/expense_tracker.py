import csv
import os
from datetime import date

# Expenses are saved next to this script
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
FIELDS = ["date", "category", "description", "amount"]
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]


# Load all expenses from the CSV file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows


# Append one expense to the CSV file
def save_expense(expense):
    new_file = not os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(expense)


def ask_amount():
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
            if amount > 0:
                return round(amount, 2)
        except ValueError:
            pass
        print("Please enter a positive number.")


def ask_category():
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {name}")
    while True:
        text = input("Category number: ").strip()
        if text.isdigit() and 1 <= int(text) <= len(CATEGORIES):
            return CATEGORIES[int(text) - 1]
        print("Invalid category.")


def add_expense(expenses):
    amount = ask_amount()
    category = ask_category()
    description = input("Description: ").strip() or "-"
    expense = {
        "date": date.today().isoformat(),
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    save_expense(expense)
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"\n{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 62)
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<15}{e['description'][:24]:<25}{e['amount']:>10.2f}")
    print("-" * 62)
    print(f"{'Total':<52}{sum(e['amount'] for e in expenses):>10.2f}")


# Show total spent per category with a simple text bar chart
def show_summary(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())

    print("\nSpending by category:")
    for category, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percent = total / grand_total * 100
        bar = "#" * int(percent / 2)
        print(f"{category:<15}{total:>10.2f}  {percent:5.1f}%  {bar}")
    print(f"\nTotal spent: {grand_total:.2f}")


# Show expenses for one month, e.g. 2026-10
def show_month(expenses):
    month = input("Month (YYYY-MM): ").strip()
    show_expenses([e for e in expenses if e["date"].startswith(month)])


def main():
    expenses = load_expenses()
    menu = {
        "1": ("Add expense", add_expense),
        "2": ("View all expenses", show_expenses),
        "3": ("View by month", show_month),
        "4": ("Category summary", show_summary),
    }

    while True:
        print("\n=== Expense Tracker ===")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        if choice in menu:
            menu[choice][1](expenses)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
