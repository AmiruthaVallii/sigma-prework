# When given a date, calculate the age between the current date and the given date.
# The function should return the age in years only.

from datetime import datetime


def calculate_age(date):
    # Convert input string into date format
    input_date = datetime.strptime(date, "%d-%m-%Y")
    # Extract day, month, year from user inputted date
    input_day = input_date.day
    input_month = input_date.month
    input_year = input_date.year
    input_date_formatted = datetime(
        input_year, input_month, input_day)

    # Get current date
    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year
    current_date_formatted = datetime(
        current_year, current_month, current_day)

    # Calculate age
    age = current_date_formatted.year - input_date_formatted.year

    # Adjust for if birthday has not occurred yet this year
    if current_month < input_month:
        age -= 1

    return age


user_date = input("Enter date in format dd-mm-yyyy: ")
print("Age in years:", calculate_age(user_date))
