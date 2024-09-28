from datetime import timedelta, datetime
# import datetime

def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0)
    print(f"Current date and time: {current_date}")
    return current_date


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = display_current_datetime()
    future_date = timedelta(days = number_of_days)
    future_date = today.date() + future_date
    print(f"Future date: {future_date}")


display_current_datetime()
calculate_future_date()