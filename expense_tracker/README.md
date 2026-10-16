# Expense Tracker – Python Mini Project

A command-line app to record your daily expenses and see where your money goes. All data is stored in a `expenses.csv` file, which you can also open in Excel or Google Sheets.

## Features

- Add expenses with amount, category and description (date is added automatically)
- View all expenses in a neat table with a total
- Filter expenses by month
- Category summary with percentages and a text bar chart
- Data saved to `expenses.csv`

## How to Run

Make sure you have **Python 3** installed. No extra packages are needed.

```bash
cd expense_tracker
python expense_tracker.py
```

## Example

```
Spending by category:
Food                450.00   45.0%  ######################
Transport           300.00   30.0%  ###############
Bills               250.00   25.0%  ############

Total spent: 1000.00
```

## Concepts Used

- `csv` module (`DictReader`, `DictWriter`)
- `datetime` module
- Dictionaries for grouping and totals
- f-string formatting for tables
- `try` / `except` for input validation
