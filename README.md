 # Personal-Finance-Tracker

This Python project allows users to manage their financial transactions through a CSV-based system. 
It provides functionalities for adding new transactions, viewing transactions within a specified date range, and visualizing income vs. expenses over time using Matplotlib.

Features:
1. Add New Transaction
Users can add new transactions specifying the date, amount, category (income or expense), and an optional description.

2. View Transactions and Summary:
Retrieve transactions that fall within a specified start and end date.
Display a summary of total income, total expenses, and net savings for the selected date range.

3. Plot Income and Expenses Over Time:
Generates a plot using Matplotlib that visualizes income and expenses over time.
Transactions are grouped by day and summed up to show trends.
Components:

4. CSV Class:
Manages interactions with the CSV file (finance_data.csv) using Pandas and CSV modules.
Initializes the CSV file if it doesn't exist.
Adds new entries to the CSV file.

5. Data Entry Functions:
Helper functions (get_date, get_amount, get_category, get_description) to interact with users and collect transaction details.
Ensures user input validation for date format, amount (non-negative), and category (income or expense).

6. Plotting Transactions:
plot_transactions(df): Function to plot income and expenses over time using Matplotlib. Utilizes Pandas for data manipulation and plotting capabilities.


Usage:
1. Adding a Transaction:
Choose option 1 to add a new transaction.
Input date, amount, category, and optional description.

2. Viewing Transactions:
Choose option 2 to view transactions within a specific date range.
Option to visualize the data as a plot if desired.

Requirements:
1. Python 3.x
2. Pandas library (pip install pandas), for mac: (pip3 install pandas)
3. Matplotlib library (pip install matplotlib)

How to Run:
Clone the repository and navigate to the project directory.
Run python main.py to start the program.
Follow the prompts to add/view transactions and generate plots.
