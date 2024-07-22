import pandas as pd  # pandas will allow us to load-in the csv file and work with it a lot easier, pd is alias for pandas
import csv  # importing the csv module (difference between library and module is that library is a collection of modules)
from datetime import datetime  # module in python to help with working with dates and times
# importing functions from the data_entry file
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt 

class CSV:  # setting up a class which will have some methods that will help us work easily with the CSV file.
    CSV_FILE = "finance_data.csv"  # creating a class variable named csv_file
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    # Initialising CSV file
    @classmethod  # decorating with the class method decorator, meaning it has access to everything in class CSV
    def initialise_csv(cls):  # creating a method, with parameter cls
        try:  # trying to read in the csv file
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:  # if file not found...we're gonna create our own file with these properties
            # a dataframe is an object within pandas that allows us to access different rows/columns from a csv file
            df = pd.DataFrame(columns=cls.COLUMNS)  # creating a dataframe
            # we need to export the dataframe into a csv file
            df.to_csv(cls.CSV_FILE, index=False)  # this line converts the dataframe we just created with the four columns into a csv file. it will save a csv file with the name "finance_data.csv" from the first line of the class

    # Adding some entries to the file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        # We need to use a csv writer to write into the file
        # Creating entry using python dictionary
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # Opening the file
        # The "with open" and "as csvfile" in the following line deals with closing the file after the two lines after it run and the dictionary is added to csv file
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # the "a" is for append, meaning that when we open the file the cursor is going to be at the end of the file so it can add more stuff
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)  # dictwriter means we're gonna take a dictionary and write that into the csv file
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # Converting all of the dates inside the date column to a datetime object
        # so we can use them to filter by different transactions
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)  # ability not just to access the individual rows but to access all of the columns
        start_date = datetime.strptime(start_date, CSV.FORMAT)  # convert from string to correct format
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)  # '&' is similar to 'and' in the python language but '&' is typically used with pandas library
        filtered_df = df.loc[mask]  # this line returns a new filtered data frame that only has the rows where the previous line was true

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()  # from the dataframe, we want to get all the rows where the category is equal to income, once I get those, I want to have all the values in the amount column and sum them
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income: .2f}")
            print(f"Total Expense: ${total_expense: .2f}")
            print(f"Net savings: ${total_income - total_expense: .2f}")
        return filtered_df


# Function that will call all the functions from data entry file in the order that we want in order to collect our data
def add():
    CSV.initialise_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


# plotting the transactions
# plotting the transactions
def plot_transactions(df):
    df.set_index("date", inplace=True)

    # income dataframe
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    # expense dataframe
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    # create plot using matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



# function to interact with user and use all the functions we've built to know what user wants 
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within the data range")
        print("3. Exit")
        choice = input("Enter your choice (1,3): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break 
        else:
            print("Invalid choice. Enter 1, 2 or 3 ")

if __name__ == "__main__":
    main()