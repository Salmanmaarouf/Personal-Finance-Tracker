# the data entry file is a place where I can write all of the functions related to getting information from the user 
from datetime import datetime


#since we have 3 instances of the format "%d-%m-%Y" and we dont want repetition, we're gonna create a constant
DATE_FORMAT = "%d-%m-%Y"
# we need to make sure for category they're gonna type i or e so we create this constant
CATEGORIES = {"I": "Income", "E": "Expense"}



# this is a returning function, meaning it will keep running until the user gives a valid date. (todays date or the valid date they entered )
# our first function is to get the date of the transaction
def get_date(prompt, allow_default = False): # the prompt is what we're going to ask the user to unput before they give us the date, the "allow_default = False" is for user to be able to hit enter if transaction was today  
    date_str = input(prompt) # prompt is the date string inputed 
    if allow_default and not date_str:
        # we return the current date in the scenario where the user didnt type any date and pressed entre for todays date 
        return datetime.today().strftime(DATE_FORMAT) # "("%d-%m-%Y")" is a format specifier, .today() returns the current local date
    # otherwise, if they enterd a date we need to check that it's valid
    try:
        valid_date = datetime.strptime(date_str,DATE_FORMAT) # checks if user inputed date is in the correct format
        return valid_date.strftime(DATE_FORMAT) # if it passes the above format then yes, its a valid date 
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)
    
    
    
    
# function to get transaction amount 
# keep calling this function until we get a valid amount 
def get_amount(): 
    try:
        amount = float(input("Enter the amount: ")) # converting input to float incase the amount inputed is deciman 
        if amount <= 0: # since we dont want user to enter a negative number. 
            raise ValueError("Amount must be a non-negative non-zero value. ")
        return amount 
    except ValueError as e:
        print(e)
        return get_amount()



# ask user if its income or expenses
# keeps calling function until we get a valid category, either I or E 
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense) ").upper() # the upper so that if user types i or e lower case it would still work 
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid category, Please enter 'I' for Income or 'E' for Expense.")
    return get_category()



# ask user for transaction description 
def get_description():
    return input("Enter a description (optional): ") # user can type anything here becasue it's optional 