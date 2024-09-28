from datetime import timedelta, datetime
# import datetime

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    return datetime.now()


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = display_current_datetime()
    future_date = timedelta(days = number_of_days)
    future_date = today + future_date
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


display_current_datetime()
calculate_future_date()